import { ObjectId } from 'mongodb';

export interface LightingRequest {
  target: ObjectId;
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

export interface Device {
  _id?: ObjectId;
  name: string;
  type: string;
  model: string;
  ip: string;
}

export interface TemperatureRequest extends LightingRequest {
  temperature: number;
}

export interface LightingPowerStatus {
  on: boolean;
}
