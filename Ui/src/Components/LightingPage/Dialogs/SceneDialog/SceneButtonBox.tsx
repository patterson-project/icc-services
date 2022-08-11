import { Box, Grid } from "@mui/material";
import React, { FC } from "react";
import {
  gridContainerStyle,
  gridItemStyle,
} from "../../../../Styles/CommonStyles";
import OperationButton from "../../../Common/OperationButton";

const buttonBoxStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  height: "100%",
  backgroundColor: "#2C2C2E",
  width: "90%",
  borderRadius: "10px",
  paddingBottom: "10px",
};

const SceneButtonBox: FC = () => {
  return (
    <Box style={buttonBoxStyle}>
      <Grid container spacing={2} style={gridContainerStyle}>
        <Grid item xs={6} style={gridItemStyle}>
          <OperationButton
            operationName={"Ocean"}
            color={"#2a5cd1"}
            onClick={() => console.log("Clicked")}
          ></OperationButton>
        </Grid>
      </Grid>
    </Box>
  );
};

export default SceneButtonBox;
