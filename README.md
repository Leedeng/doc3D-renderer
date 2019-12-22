
# doc3D-renderer
Doc3D is the first 3D dataset focused on document unwarping with realistic paper warping and renderings.
<p align="center">
  <img src="data.gif">
</p>
This repository contains all the rendering codes of doc3D. 
The download scripts of the dataset is available in [doc3D-dataset](https://github.com/cvlab-stonybrook/doc3D-dataset) repo. 

### Instructions to render your own data:
- Step 1: Generate Augmentated Text
	- `cd tex`
	- `python texgenerator.py`
- Step 2: Check the assets in `objs.csv`,`envs.csv`, and `texs.csv`.
If you want to modify text images, PLEASE DO NOT DELETE "tex/1.jpg".
- Step 3 : Render images:
        - `cd ..`
	- `blender --background --python render_meshGT.py -- 10 1 20`
1,20 refer to startID and EndID. Total of (20-1=19) images will be generated
- Step 5 : Render GT images:
	- `python groudntruthgen.py`
gt1,gt2 and ground images folders(but there are different!). img(normal),img_s(stamp&stain),img_b(blur) are source images folders.	
### Citation:
If you use the dataset or this code, please consider citing our work-
```
@inproceedings{SagnikKeICCV2019, 
Author = {Sagnik Das*, Ke Ma*, Zhixin Shu, Dimitris Samaras, Roy Shilkrot}, 
Booktitle = {Proceedings of International Conference on Computer Vision}, 
Title = {DewarpNet: Single-Image Document Unwarping With Stacked 3D and 2D Regression Networks}, 
Year = {2019}}   
```
#### Acknowlegement: 
Thanks to the awesome software, [Blender](https://www.blender.org/), thanks to it's developers and also to the super awesome [community](https://blender.stackexchange.com/).

