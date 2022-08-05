import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./index.css";
import DevicePage from "./Components/DevicePage/DevicePage";
import HomePage from "./Components/HomePage/HomePage";
import LightingPage from "./Components/LightingPage/LightingPage";

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
