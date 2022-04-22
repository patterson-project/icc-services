
export interface LightingRequest {
    operation: string;
}

export interface RainbowRequest extends LightingRequest {
    wait_ms?: number;
}

export interface BrightnessRequest extends LightingRequest {
    brightness: number;
};

export interface HslaRequest extends LightingRequest {
    h: number;
    s?: number;
    l?: number;
    a?: number;
};
