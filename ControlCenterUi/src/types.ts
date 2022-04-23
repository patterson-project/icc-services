
export interface LightingRequest {
    operation: string;
}

export interface RainbowRequest extends LightingRequest {
    delay: number;
}

export interface BrightnessRequest extends LightingRequest {
    brightness: number;
    delay: number;
};

export interface HsvRequest extends LightingRequest {
    h: number;
    s?: number;
    v?: number;
};
