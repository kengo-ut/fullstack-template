const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

module.exports = {
  backend: {
    output: {
      mode: "tags-split",
      target: "src/gen/backend.ts",
      schemas: "src/gen/schema",
      clean: true,
    },
    hooks: {
      afterAllFilesWrite: () => {
        const genDir = path.resolve(__dirname, "src/gen");

        const subDirs = fs.readdirSync(genDir).filter((name: string) => {
          const fullPath = path.join(genDir, name);
          return fs.statSync(fullPath).isDirectory();
        });

        subDirs.forEach((dirName: string) => {
          const targetFile = path.join(genDir, dirName, `${dirName}.ts`);
          if (fs.existsSync(targetFile)) {
            fs.appendFileSync(
              targetFile,
              `\naxios.defaults.baseURL = process.env.NEXT_PUBLIC_API_BASE_URL;\n`
            );
            console.log(`✅ axios.defaults.baseURL を ${dirName}.ts に追加しました！`);
          }
        });

        try {
          execSync("npx prettier --write src/gen", { stdio: "inherit" });
          console.log("✅ Prettier で整形しました！");
        } catch (err) {
          console.error("❌ Prettier の整形に失敗しました:", err);
          throw err;
        }
      },
    },
    input: {
      target: "../backend/openapi.json",
    },
  },
};
