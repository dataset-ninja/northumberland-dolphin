Dataset **NDD20** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/y/t/Yx/9ytaPSbFuIpQNBKnL8AKhYVt1CxQjmzf8eptnn75pF4q2Br2NB1pt3hfDOIciU14wHfdJkCL53ID5sW9LAuTRr52qwFQiGAGrNJBVnQLWiBINx5xhSHV7gXeVzj5.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='NDD20', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://data.ncl.ac.uk/articles/dataset/NDD20_zip/12357383?backTo=/collections/The_Northumberland_Dolphin_Dataset_2020/4982342).