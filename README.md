# Remaster Visualizing Data (Ben Fry) with Processing Py5  

## Intro

1. Basic Processing
- size (size, width, height, renderer?)
- Image and String import

2. Functions in Processing map to Daviz Process

Acquire : loadStrings(), loadBytes()
Parse : split()
Filter : for( ), if (item[i].startsWith( ))
Mine : min(), max(), abs()
Represent : map(), beginShape(), endShape()
Refine : fill( ), strokeWeight(), smooth()
Interact : mouseMoved(), mouseDragged(), keyPressed()

py5
Acquire : 
load_bytes() - Load byte data from a file or URL.
load_json() - Load a JSON data file from a file or URL.
load_pickle() - Load a pickled Python object from a file.
load_strings() - Load a list of strings from a file or URL.
parse_json() - Parse serialized JSON data from a string.
select_folder() - Opens a file chooser dialog to select a folder.
select_input() - Open a file chooser dialog to select a file for input.

Parse & Filter : Pandas
Mine : Pandas & Numpy
Repersent : remap, 
begin_closed_shape() - This method is used to start a custom closed shape.
begin_contour() - Use the begin_contour() and end_contour() methods to create negative shapes within shapes such as the center of the letter ‘O’.
begin_shape() - Using the begin_shape() and end_shape() functions allow creating more complex forms.
bezier_vertex() - Specifies vertex coordinates for Bezier curves.
bezier_vertices() - Create a collection of bezier vertices.
curve_vertex() - Specifies vertex coordinates for curves.
curve_vertices() - Create a collection of curve vertices.
end_contour() - Use the begin_contour() and end_contour() methods to create negative shapes within shapes such as the center of the letter ‘O’.
end_shape() - The end_shape() function is the companion to begin_shape() and may only be called after begin_shape().
quadratic_vertex() - Specifies vertex coordinates for quadratic Bezier curves.
quadratic_vertices() - Add a collection of quadratic vertices.
vertex() - Add a new vertex to a shape.
vertices() - Add a collection of vertices to a shape.

Refine:
fill() - Sets the color used to fill shapes.
no_fill() - Disables filling geometry.
no_stroke() - Disables drawing the stroke (outline).
stroke() - Sets the color used to draw lines and borders around shapes.
stroke_weight() - Sets the width of the stroke used for lines, points, and the border around shapes.
stroke_cap() - Sets the style for rendering line endings.
stroke_join() - Sets the style of the joints which connect line segments.
pop_style() - The push_style() function saves the current style settings and pop_style() restores the prior settings; these functions are always used together.
push_style() - The push_style() function saves the current style settings and pop_style() restores the prior settings.
push() - combines push_style() and push_matrix() The push() function saves the current drawing style settings and transformations, while pop() restores these settings.
pop() - combines pop_style() and pop_matrix() The pop() function restores the previous drawing style settings and transformations after push() has changed them.
smooth() - Draws all geometry with smooth (anti-aliased) - edges. Must be used just after size().
no_smooth() - Draws all geometry and fonts with jagged (aliased) - edges and images with hard edges between the pixels when enlarged rather than interpolating pixels.

Interaction

mouse_pressed() - If defined, it will be called once when a mouse button is pressed.
mouse_released() - If defined, it will be called once when a mouse button is pressed.
mouse_clicked() - If defined, it will be called once when a mouse button is clicked.
mouse_dragged() - If defined, it will be called many times as the mouse is moved while pressed.
mouse_wheel() - If defined, it will be called as the mouse wheel is rolled.
mouse_moved() - If defined, it will be called many times as the mouse is moved.
mouse_entered() - If defined, it will be called when the mouse enters the sketch area.
mouse_exited() - If defined, it will be called when the mouse leaves the sketch area.
Py5MouseEvent Class - A Py5MouseEvent object will be passed to user-defined mouse event functions.

key_pressed() - If defined, it will be called once when a keyboard key is pressed.
key_released() - If defined, it will be called once when a keyboard key is released.
key_typed() - If defined, it will be called once when a keyboard key is pressed and released.
Py5KeyEvent Class - A Py5KeyEvent object will be passed to user-defined keyboard event functions.

## Features Not Yet Implemented

1. Map (Integrator Class)
2. Time Series (Tab & Integrator Class)