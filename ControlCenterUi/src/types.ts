
export interface ColorChangeRequest {
    operation: string;
}

export interface RainbowRequest extends ColorChangeRequest {
    wait_ms?: number;
}

export interface BrightnessRequest extends ColorChangeRequest {
    brightness: number;
};

export interface HslaRequest extends ColorChangeRequest {
    h: number;
    s?: number;
    l?: number;
    a?: number;
};
