/*{
        "DESCRIPTION": "persistent buffer, adapted for Touchdesigner 2022.24200",
        "CREDIT": "by luisarandas",
        "CATEGORIES": [
                "Blur, Ping-Pong Delay, Persistent Buffer"
        ],
        "INPUTS": [
                {
                        "NAME": "inputImage",
                        "TYPE": "image"
                },
                {
                        "NAME": "blurAmount",
                        "TYPE": "float",
                        "DEFAULT": 0.0
                }
        ],
        "PERSISTENT_BUFFERS": [
                "bufferVariableNameA"
        ],
        "PASSES": [
                {
                        "TARGET":"bufferVariableNameA",
                        "FLOAT": true
                },
                {

                }
        ]

}*/

// #version 430 // tested

void main() {

        vec4 freshPixel = IMG_NORM_PIXEL(inputImage, gl_FragCoord.xy/RENDERSIZE);
        vec4 stalePixel = IMG_NORM_PIXEL(bufferVariableNameA, gl_FragCoord.xy/RENDERSIZE);
        gl_FragColor = mix(freshPixel, stalePixel, blurAmount);
}

