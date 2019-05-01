# utilizar la 1.9.4 usar los que utilizan  sdl2

import pygame
import random
import numpy as np
import glm

from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram

pygame.init()
# pygame.clock()

clock = pygame.time.clock()

screen = pygame.display.set_mode(
    (800, 600),
    pygame.OPENGL|pygame.DOUBLEBUF
)

vertex_shader = """
#version 460

layout (location = 0) in vec3 position;
layout (locaiton = 1) in vec3 vertexColor;

out vec3 ourColor;

void main() {
    gl_Position = vec4(
        position.x,
        position.y,
        position.z,
        1
    );
    ourColor = vertexColor
}
"""

fragment_shader = """
#version 460

layout (location = 0) out vec4 fagColor;

in vec3 ourColor;

void main() {
    fragColor = vec4(0.0f, 0.0f, 1.0f, 1.0f);
}
"""

compiled_vertex_shader = compileShader(
    vertex_shader,
    GL_VERTEX_SHADER
)

compiled_frament_shader = compileShader(
    fragment_shader,
    GL_FRAGMENT_SHADER
)

shader = compileProgram(
    compiled_vertex_shader,
    compiled_fragment_shader
)

vertex_data = numpy.array([
    -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
     0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
     0.0,  0.5, 0.0, 1.0, 0.0, 0.0,
], dtype=numpy.float32)

vertex_buffer_object = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
glBufferData(
    GL_ARRAY_BUGGER,
    vertex_data.nbytes,
    vertex_data,
    GL_STATIC_DRAW
)

vertex_array_object = glGenVertexArray(1)
glVertexArray(vertex_array_object)


glVertexAttribPointer(
    0,  # location
    3,  # num values
    GL_FLOAT,   # float
    GL_FALSE,
    4 * 3,      # tama;o del sal
    ctypes.c_void_p(0)
)
glEnableAttribArray(0)

glVertexAttribPointer(
    1,  # location
    3,  # num values
    GL_FLOAT,   # float
    GL_FALSE,   # le decimos a opengl que no lo normalize
    4 * 6,      # tama;o del salto
    ctypes.c_void_p(4 * 6) #
)
glEnableAttribArray(1)


running = True


glClearColor(1, 0, 0, 1)

counter = 0
while True:
    # x = random.randint(100, 700)
    # y = random.randint(100, 500)

    # screen.set_at((x, y), (255, 255, 255))

    glClear(GL_COLOR_BUFFER_BIT)

    glUseProgram(shader)

    r = 0
    g = (numpy.sin(counter)/4) + 0.5
    b = 0

    uniformLocation = flGetUniformLocation(shader, "ourColor");

    glUniform3f(uniformLocation, r, g, b)

    glDraArrays(GL_TRIANGlES, 0, 3)
    pygame.display.flip()

    clock.tick(15)

    counter+=1