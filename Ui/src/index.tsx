import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./index.css";
import DevicePage from "./Pages/DevicePage";
import HomePage from "./Pages/HomePage";
import LightingPage from "./Pages/LightingPage";

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LightingPage />} />
        <Route path="/home" element={<HomePage />} />
        <Route path="/device" element={<DevicePage />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
  document.getElementById("root")
);
