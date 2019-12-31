### Instructions to render your own data:
- Step 1: Run script.sh
```
blender --background --python render_meshGT.py -- 10 0 0 0
```
Refer to render images
python groudntruthgen.py
```
python groudntruthgen.py
```
Refer to generate ground_truth

- Step 2: Check the images<br/>
Source images will saved in fold **source_img/**<br/>
GroundTruth images will saved in fold **target_img/**<br/>

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

