export interface LightingRequest {
  operation: string;
}

export interface BrightnessRequest extends LightingRequest {
  brightness: number;
}

export interface SceneRequest extends LightingRequest {
  scene: string;
}

export interface HsvRequest extends LightingRequest {
  h: number;
  s?: number;
  v?: number;
}

export interface TemperatureRequest extends LightingRequest {
  temperature: number;
}

export interface LightingPowerStatus {
  on: boolean;
}
