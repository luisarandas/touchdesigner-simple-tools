// BarrelDistortion.frag
// 21-09-2024 luisarandas

// Uniforms for controlling distortion
uniform float strength;
uniform float power;

// 'sTD2DInputs' sampler2D array and 'vUV' varying are declared elsewhere

// Function to apply barrel distortion
vec2 barrelDistortion(vec2 coord, float amt) {
    vec2 centeredCoord = coord - 0.5;
    float distanceSquared = dot(centeredCoord, centeredCoord);
    return coord + centeredCoord * pow(distanceSquared, power) * amt * strength;
}

out vec4 fragColor;

void main() {
    vec2 uv = vUV.st;

    // Distortion amounts
    const float distortionAmounts[12] = float[](
        0.0, 0.2, 0.4, 0.6,
        0.8, 1.0, 1.2, 1.4,
        1.6, 1.8, 2.0, 2.2
    );

    // Initialize accumulator for color
    vec4 accumulatedColor = vec4(0.0);

    // Sample texture with different distortion amounts
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[0]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[1]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[2]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[3]));
    
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[4]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[5]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[6]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[7]));
    
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[8]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[9]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[10]));
    accumulatedColor += texture(sTD2DInputs[0], barrelDistortion(uv, distortionAmounts[11]));

    // Average the accumulated color
    fragColor = accumulatedColor / 12.0;
}
