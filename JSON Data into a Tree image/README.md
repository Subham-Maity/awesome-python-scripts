### 1. This .py file you want to run should have the JSON data in the same location
### 2. Change the name of your json file or change the name here 
```py
# Load JSON data from file
with open('example.json', 'r') as f: 
    data = json.load(f)
```
- example.json to your_jsonfilename.json


#### Small Guide

**********
1. Install Graphviz: You can install Graphviz by following the instructions on their website (https://graphviz.org/download/).
2. Install the Graphviz Python package: Open your terminal or command prompt and type `pip install graphviz` to install the Graphviz Python package.
3. Write a Python script: In your IDE or Visual Studio Code, create a new Python file and write a script that converts your JSON data into a tree image using Graphviz. 
4. Run the script: Save the file and run it using your Python interpreter (e.g., by typing `python <filename>.py` in your terminal or command prompt). This should generate a tree image from your JSON data.



### Tips

- you can save the generated tree image in PNG format with a transparent background.

```py
# Save the generated image to a file
dot.format = 'png'
dot.attr(bgcolor='transparent')
dot.render('tree.gv', view=True)
```
- If the generated image still has a white background instead of being transparent, you can try setting the bgcolor attribute for both the graph and the nodes to 'transparent':

```py
# Save the generated image to a file
dot.format = 'png'
dot.attr(bgcolor='transparent')
dot.node_attr.update(bgcolor='transparent')
dot.render('tree.gv', view=True)
```


- If you want to invert the colors of the tree (e.g., make the text white and the background black), you can do this by setting the fontcolor and bgcolor attributes for both the graph and the nodes:

```py
# Save the generated image to a file
dot.format = 'png'
dot.attr(bgcolor='black', fontcolor='white')
dot.node_attr.update(bgcolor='black', fontcolor='white')
dot.render('tree.gv', view=True)
```

- you can improve the quality of the generated PNG image and make it more visually appealing by customizing various attributes of the graph, nodes, and edges.

  - Increase the resolution of the image: You can increase the resolution of the generated image by setting the dpi attribute for the graph. For example, to generate an image with a resolution of 300 DPI, you can add this line to your script:
  
  ```py
  dot.attr(dpi='300')
  ```

  - Change the font: You can change the font used for the text in the graph by setting the fontname attribute for both the graph and the nodes. For example, to use the Helvetica font, you can add these lines to your script:
  
  ```py

   dot.attr(fontname='Helvetica')
   dot.node_attr.update(fontname='Helvetica')
  ```

  - Customize node shapes and colors: You can customize the shape and color of individual nodes by setting their shape, style, fillcolor, and other attributes. For example, to make all nodes elliptical and filled with a gradient from white to light blue, you can add these lines to your script:
  
  ```py
  dot.node_attr.update(shape='ellipse', style='filled', fillcolor='white:lightblue')
  ```

> These are just a few examples of how you can customize the appearance of your tree. Graphviz provides many more attributes that you can use to create visually appealing graphs. You can find more information in their documentation (https://graphviz.org/doc/info/attrs.html).




