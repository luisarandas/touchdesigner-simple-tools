// RandomGrid.frag
// 21-09-2024 luisarandas
//
// This fragment shader divides the screen into a grid based on the number of input audio files.
// Each cell in the grid represents one audio file, colored uniquely.
// If the grid has more cells than audio files, extra cells are rendered as transparent.
//
// TouchDesigner GLSL TOP expects:
// - A varying vec2 `vUV` containing the normalized texture coordinates.
// - Output color via `fragColor` using the `TDOutputSwizzle` function.

out vec4 fragColor;

// Uniform to control the number of audio files (number of rectangles)
uniform int input_audio_files; // Controls the number of rectangles in the grid

// Assuming vUV is provided by TouchDesigner

// Function to generate a pseudo-random float based on input coordinates
float rand(vec2 co)
{
    // A simple hash function using sine and dot product
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

void main()
{
    // Ensure the number of audio files is at least 1
    int n = max(input_audio_files, 1);

    // Compute the number of rows and columns
    // Rows: floor(sqrt(n))
    // Columns: ceil(n / rows)
    float sqrt_n = sqrt(float(n));
    int rows = int(floor(sqrt_n));
    if (rows < 1) rows = 1; // Ensure at least one row
    int cols = int(ceil(float(n) / float(rows)));

    // Calculate the size of each grid cell in UV space (0.0 to 1.0)
    vec2 cellSize = vec2(1.0 / float(cols), 1.0 / float(rows));

    // Determine the current fragment's column and row indices
    int col = int(floor(vUV.x / cellSize.x));
    int row = int(floor(vUV.y / cellSize.y));

    // Clamp indices to ensure they are within grid bounds
    col = clamp(col, 0, cols - 1);
    row = clamp(row, 0, rows - 1);

    // Calculate a unique index for each cell
    // Indexing starts from 0 (top-left) to (rows * cols - 1) (bottom-right)
    int cell_index = row * cols + col;

    // If the current cell index is greater than or equal to the number of audio files,
    // render the cell as transparent
    if (cell_index >= n)
    {
        fragColor = vec4(0.0, 0.0, 0.0, 0.0); // Transparent
    }
    else
    {
        // Unique cell coordinates for color generation
        vec2 cellCoord = vec2(float(col), float(row));

        // Generate a pseudo-random color for the cell
        vec3 color = vec3(
            rand(cellCoord + vec2(0.0, 0.0)), // Red component
            rand(cellCoord + vec2(1.0, 0.0)), // Green component
            rand(cellCoord + vec2(0.0, 1.0))  // Blue component
        );

        // Assign the color with full opacity
        fragColor = vec4(color, 1.0);
    }
}