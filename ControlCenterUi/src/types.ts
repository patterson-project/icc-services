
export interface LightingRequest {
    operation: string;
}

export interface RainbowRequest extends LightingRequest {
    wait_ms?: number;
}

export interface BrightnessRequest extends LightingRequest {
    brightness: number;
};

export interface HsvRequest extends LightingRequest {
    h: number;
    s?: number;
    v?: number;
};
