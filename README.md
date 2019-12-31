### Instructions to render your own data:
- Step 1: Run script.sh
```python
blender --background --python render_meshGT.py -- 10 0 0 0
python groudntruthgen.py
```

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

