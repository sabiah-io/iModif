# iModif

imodif is an image brightness modifier. This module is mainly meant to reduce or increase the brightness of images. It either brightens, darkens or dims images and uses libraries like numpy and opencv., hence ensure these packages are installed alongside imodif. [Github](https://github.com/jellyCodee/iModif) documentation.


## Why?
I built this module because I needed a package, module or function that could help me darken my images to simulate night time but I didn't seem to find anything simple enough to meet my need. Everything was so complex with a lot of complicated mathematics. Nothing really fit what I wanted to do with my images so I had to build one to do it and perhaps help anyone out there with a similar need to mine.


## Installation

You can install imod from [PyPi](https://pypi.org/) or using python pip installer
```
pip install imodif
```


## Importing
Importing the package modules is as follows
```
from imodif import dark, dim, bright
```


## How to use

```
img_path = r"C:\Users\malon\Desktop\assests\Stlogo.png"

dark.dark(img_path, degree=9, show=True, show_original=True)
```

<img src="/images/dark.png" width="600" height="400">


```
img_path = r"C:\Users\malon\Desktop\assests\Stlogo.png"

bright.bright(img_path, degree=9, show=True, show_original=True)
```

<img src="/images/bright.png" width="600" height="400">


```
img_path = r"C:\Users\malon\Desktop\assests\Stlogo.png"

dim.dim(img_path, degree=9, show=True, show_original=True)
```

<img src="/images/dim.png" width="600" height="400">


Other methods include 
```
dark.dark_to_folder(_parameters_)
bright.bright_to_folder(_parameters_)
dim.dim_to_folder(_parameters_)
```

**NB**: Press 0 on your keyboard to close opened images.

imodif is really simple to use. There are basically just 6 methods you'll be calling.
First three is `dark`, `bright` and `dim`. These methods have the following parameters.

`image`(required): The image you wish to brighten. This should be the absolute path to the image.

`degree`: The degree of darkness you want. Values range from 1 to 15 with 1=lowest darkness and 15(10 for the dim method)=highest darkness. Default is set to 1.

`show`: True to show the modified image using cv2.imshow, False to not show modified image. Defaults to False.

`show_original`: True to show original image alonside modified image, False to not show original image but modified only. Defaults to False.


The first three methods take a single image and returns the modified numpy array or image based on the parameters set. This helps give a fair idea on what images will look like before applying them on multiple images which the next three handles.


The next `dark_to_folder`, `dim_to_folder` and `bright_to_folder` take the path or directory of a folder containing images, applies the required modification to the images and saves them in a new folder specified in the parameter 'folder_name'. Dafault name is "modified. The following parameters can be set for these methods.

`images_path`(required): The absolute path of the folder containing the images.

`file_extension`(required): The extension name of the files in the folder, eg. jpg, png etc.... Must be a string value.

`folder_name`: Name of the newly created folder that contains the modified images. Defaults to 'modified'.

`lowest_degree`: The least value of degree of modification to apply to the images. Defaults to 1.

`highest_degree`: The highest value of degree of modification to apply to the images. Defaults to 5. Limit is 15(10 for dim_to_folder).

`add_original`: True to add original images to modified ones in the folder, False to not. Defaults to False.

`fperc`: Percentage of images in the folder to modify. Range between 0 to 1.

`shuffle`: True to shuffle up the modified and original images in the folder, False to not. Defaults to False.


The lowest and highest degree parameters are used to setup a range that applies random degrees of modifications to the images, hence all the images do not have the same degree of modification i.e., brightness, darkness or dimness. With this there is no need to manually apply dark, bright, dim filters to images one by one. You get to apply these filters to bulk images at the same time with varying degrees of contrast.