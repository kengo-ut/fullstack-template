"use client";
import Image from "next/image";
import nextConfig from "../../next.config";
const BASE_PATH = nextConfig.basePath || "";
import { useState } from "react";
import React from "react";

const Sample = () => {
  const [color, setColor] = useState("text-blue-500");

  return (
    <div>
      <Image src={`${BASE_PATH}/file.svg`} alt="file" width={200} height={200} />
      <div className={`text-9xl font-bold ${color}`}>Hello, world!</div>
      <button
        onClick={() => {
          if (color === "text-blue-500") setColor("text-red-500");
          else setColor("text-blue-500");
        }}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
      >
        Change color
      </button>
    </div>
  );
};

export default Sample;
