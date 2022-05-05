export interface LightingRequest {
  operation: string;
}

export interface BrightnessRequest extends LightingRequest {
  brightness: number;
}

export interface HsvRequest extends LightingRequest {
  h: number;
  s?: number;
  v?: number;
}

export interface ColorTempRequest extends LightingRequest {
  temperature: number;
}