import OpenGL.GL.shaders
from pyglet.gl import *
from test_gl import *




class Triangle(object):
	def __init__(self):
		self.verticies = pyglet.graphics.vertex_list(3, 
								('v3f', [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.0,0.5,0.0]), 
								('c3B', [100,200,220, 200,110,100, 100,250,100])
								)


class Quad:
	def __init__(self):
		self.verticies = pyglet.graphics.vertex_list_indexed(4, 
									[0, 1, 2, 2, 3, 0],
									('v3f', [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]),
									('c3f', [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,1.0,1.0])
									)

class Quad2:
	def __init__(self):
		self.indicies = [0, 1, 2, 2, 3, 0]
		self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
		self.color = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,1.0,1.0]

		self.verticies = pyglet.graphics.vertex_list_indexed(4, self.indicies, ('v3f', self.vertex), ('c3f', self.color))


class Quad3:
	def __init__(self):
		self.indicies = [0, 1, 2, 2, 3, 0]
		self.vertex = [-0.5,-0.5,0.0, 0.5,-0.5,0.0, 0.5,0.5,0.0, -0.5,0.5,0.0]
		self.color = [1.0,0.0,0.0, 0.0,1.0,0.0, 0.0,0.0,1.0, 1.0,1.0,1.0]

		self.verticies = pyglet.graphics.draw_indexed(4, GL_TRIANGLES, self.indicies, ('v3f', self.vertex), ('c3f', self.color))

	def render(self):
		self.verticies = pyglet.graphics.draw_indexed(4, GL_TRIANGLES, self.indicies, ('v3f', self.vertex), ('c3f', self.color))



class MyWindow(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.set_minimum_size(400, 300)
		glClearColor(0.2, 0.3, 0.2, 1.0)

		#self.triangle = Triangle()
		#self.quad = Quad()
		#self.quad2 = Quad2()
		#self.quad3 = Quad3()

		self.triangle = Triangle2()





	def on_draw(self):
		self.clear()
		glDrawArrays(GL_TRIANGLES, 0)
		#self.triangle.verticies.draw(GL_TRIANGLES)
		#self.quad.verticies.draw(GL_TRIANGLES)
		#self.quad2.verticies.draw(GL_TRIANGLES)
		#self.quad3.render()



	def on_resize(self, width, height):
		glViewport(0, 0, width, height)


if __name__ == "__main__" :
	window = MyWindow(1280, 720, "MyWindow", resizable=True)
	pyglet.app.run()