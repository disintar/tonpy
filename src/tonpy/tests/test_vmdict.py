from pathlib import Path
import sys
from random import random
from time import time

import pytest

path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from tonpy.types.vmdict import VmDict
from tonpy.types.cellbuilder import CellBuilder, CellSlice, Cell

reveal_dict_boc = "te6ccuICAhkAAQAAG3wAAAAQAB4ALAA6AEgAVgBkALYBCAFaAawBugHIAhoCbAK+AxADHgMsAzoDSANWA2QDiAOsA9AD9AQCBBAENARYBHwEoASuBNIE4ATuBRIFOAVcBYAFjgWcBaoFuAXGBdQF4gXwBhQGOAZcBoAGjgacBsAG5AcKBzAHPgdMB1oHaAeOB7IH1gf6CAgIFgg4CFwIgAikCLIIwAjOCNwI6gj4CRwJQAlkCYgJlgmkCcoJ8AoUCjgKRgpUCmIKcAqUCrgK3AsACw4LHAtAC2QLiAuqC7gLxgvUC+IL8Av+DAwMGgw8DGAMhAyoDLYMxAzoDQwNMA1UDWINcA1+DYwNsg3WDfoOIA4uDjwOYA6EDqgOzA7aDugO9g8EDxIPIA9ED2YPig+wD74PzA/wEBIQNhBcEGoQeBCGEJQQuhDgEQQRKBE2EUQRaBGOEbIR1hHkEfISABIOEhwSKhI4EkYSahKOErIS2BLmEvQTGBM8E2ITiBOWE6QTshPAE+QUCBQsFFAUXhRsFJAUtBTaFP4VDBUaFSgVNhVEFVIVdhWaFb4V5BXyFgAWJhZKFm4WkhagFq4WvBbKFu4XFBc6F14XbBd6F6AXxBfoGAwYGhgoGDYYRBhSGGAYbhh8GKAYxhjsGRAZHhksGVAZdBmYGbwZyhnYGeYZ9BoYGjwaYBqGGpQaohrIGuwbEBs0G0IbUBteG2wbehuIG6wb0Bv0HBgcJhw0HFgcfBygHMQc0hzgHO4c/B0iHUYdah2OHZwdqh3OHfIeFh46HkgeVh5kHnIegB6OHpweqh7OHvIfFh86H0gfVh98H6Afxh/qH/ggBiAUICIgRiBqII4gsiDAIM4g9CEaIT4hYiFwIX4hjCGaIaghtiHaIf4iIiJGIlQiYiKGIqoiziL0IwIjECMeIywjUCN2I5ojviPMI9oj/iQiJEYkaiR4JIYklCSiJLAkviTMJNok/iUkJUolbiV8JYolsCXUJfgmHCYqJjgmRiZUJngmnCbAJuQm8icAJyQnSCdsJ5InoCeuJ7wnyifYJ+YoCiguKFIodiiEKJIouCjcKQApJCkyKUApTilcKYAppCnIKe4p/CoKKi4qUip2Kpwqqiq4KsYq1CriKvAq/isMKzArVCt4K5wrqiu4K9wsACwkLEgsVixkLHIsgCykLMgs7i0SLSAtLi1SLXYtnC3ALc4t3C3qLfguBi4ULjguXC6ALqYutC7CLuYvCi8uL1IvYC9uL3wvii+uL9Iv9jAaMCgwNjBaMH4wojDIMNYw5DDyMQAxDjEcMSoxODFcMYAxpDHIMdYx5DIKMi4yVDJ4MoYylDKiMrAy1DL4Mx4zRDNSM2AzhDOoM84z8jQANA40HDQqNDg0RjRsNJA0tDTYNOY09DUYNTw1YDWENZI1oDWuNbw14DYENig2TDZaNmg2jDawNtQ2+AIDzeAAAQACAgEgAAMABAIByQARABICASAABQAGAgEgAAsADAIBIAAHAAgCASAACQAKEgH40kb53rsb+r4AwvnZtzx4F2vh99+TJaYJky4gS0cdsQAFIAApACoSAbQbsPt5afbVz9ze+4TpaJvisj9c9WAfGQ8G3g4yeMkGAAUgAGcAaBIB1uDhV6Wfq3O/NnMmJE5lA6S9jv0iKDMJDrk/89t6n0QABSAApQCmEgEg5hNyeUgcFBlGIGyDWZ8odvyTac0L9a1XyCkwrHTfNgAFIADjAOQCASAADQAOAgEgAA8AEBIBwNm6wM+Dx0HZ+gMUfRySmR3Skyli18+gQY173pxat+wABSABIQEiEgE+xsfpifme5vqkvVKIFAchS/6E0T/fuLGY+jipwFLrTAAFIAFfAWASAchytl2JZ2dIg4bOhwaP3gHBJ1JmQZYQBftmyJMxoPR0AAUgAZ0BnhIBKQEj59uRwp2NRCFnm4nuO1a/qfOb9dyJrQ9Yr2CR81oABSAB2wHcAgEgABMAFAIBIAAhACICASAAFQAWAgEgABsAHAIBIAAXABgCASAAGQAaAB8cmV2ZWFsXzc5Ni5qc29ugAB8cmV2ZWFsXzc5Ny5qc29ugAB8cmV2ZWFsXzc5OC5qc29ugAB8cmV2ZWFsXzkxMi5qc29ugAgEgAB0AHgIBIAAfACAAHxyZXZlYWxfOTAxLmpzb26AAHxyZXZlYWxfODAxLmpzb26AAHxyZXZlYWxfODAyLmpzb26AAHxyZXZlYWxfODAzLmpzb26ACASAAIwAkAB/TkyuzKwti+cGBwXNTm3t0AgEgACUAJgIBIAAnACgAHxyZXZlYWxfODA0Lmpzb26AAIRyZXZlYWxfMTEwNi5qc29ugAB8cmV2ZWFsXzgwNi5qc29ugAB8cmV2ZWFsXzgzMy5qc29ugAgEgACsALAIBIABJAEoCASAALQAuAgEgADsAPAIBIAAvADACASAANQA2AgEgADEAMgIBIAAzADQAHxyZXZlYWxfODIyLmpzb26AAHxyZXZlYWxfODQxLmpzb26AAHxyZXZlYWxfMzMxLmpzb26AAHxyZXZlYWxfMjMwLmpzb26ACASAANwA4AgEgADkAOgAfHJldmVhbF81NzIuanNvboAAfHJldmVhbF81NjkuanNvboAAhHJldmVhbF8xMDEzLmpzb26AAIRyZXZlYWxfMTA5NC5qc29ugAgEgAD0APgIBIABDAEQCASAAPwBAAgEgAEEAQgAhHJldmVhbF8xMDc3Lmpzb26AAHxyZXZlYWxfMzI5Lmpzb26AAHxyZXZlYWxfOTE1Lmpzb26AAHxyZXZlYWxfOTc5Lmpzb26ACASAARQBGAgEgAEcASAAdHJldmVhbF8xMy5qc29ugAB8cmV2ZWFsXzgxNi5qc29ugAB8cmV2ZWFsXzU5MS5qc29ugAB8cmV2ZWFsXzQ1OC5qc29ugAgEgAEsATAIBIABZAFoCASAATQBOAgEgAFMAVAIBIABPAFACASAAUQBSAB8cmV2ZWFsXzI3My5qc29ugAB8cmV2ZWFsXzUzMy5qc29ugAB8cmV2ZWFsXzIwMi5qc29ugAB8cmV2ZWFsXzk1NC5qc29ugAgEgAFUAVgIBIABXAFgAIRyZXZlYWxfMTA5Mi5qc29ugACEcmV2ZWFsXzEwMjUuanNvboAAfHJldmVhbF81MjYuanNvboAAfHJldmVhbF85MzkuanNvboAIBIABbAFwCASAAYQBiAgEgAF0AXgIBIABfAGAAHxyZXZlYWxfODExLmpzb26AAHxyZXZlYWxfODU4Lmpzb26AAHxyZXZlYWxfMTQxLmpzb26AAHxyZXZlYWxfNTU2Lmpzb26ACASAAYwBkAgEgAGUAZgAfHJldmVhbF85MjEuanNvboAAfHJldmVhbF8zMzguanNvboAAfHJldmVhbF84OTMuanNvboAAdHJldmVhbF84Ni5qc29ugAgEgAGkAagIBIACHAIgCASAAawBsAgEgAHkAegIBIABtAG4CASAAcwB0AgEgAG8AcAIBIABxAHIAHRyZXZlYWxfMzMuanNvboAAfHJldmVhbF84OTEuanNvboAAfHJldmVhbF81NzkuanNvboAAfHJldmVhbF85MjYuanNvboAIBIAB1AHYCASAAdwB4AB8cmV2ZWFsXzE0Ny5qc29ugAB8cmV2ZWFsXzM3OS5qc29ugAB8cmV2ZWFsXzkxNi5qc29ugAB8cmV2ZWFsXzk4MS5qc29ugAgEgAHsAfAIBIACBAIICASAAfQB+AgEgAH8AgAAhHJldmVhbF8xMDUwLmpzb26AAHxyZXZlYWxfODEwLmpzb26AAHxyZXZlYWxfNDM0Lmpzb26AAIRyZXZlYWxfMTA1MS5qc29ugAgEgAIMAhAIBIACFAIYAHxyZXZlYWxfOTUwLmpzb26AAHxyZXZlYWxfOTg3Lmpzb26AAHxyZXZlYWxfMjU3Lmpzb26AAHxyZXZlYWxfODY0Lmpzb26ACASAAiQCKAgEgAJcAmAIBIACLAIwCASAAkQCSAgEgAI0AjgIBIACPAJAAHxyZXZlYWxfOTQwLmpzb26AAHRyZXZlYWxfOTUuanNvboAAfHJldmVhbF85MjAuanNvboAAhHJldmVhbF8xMTA5Lmpzb26ACASAAkwCUAgEgAJUAlgAfHJldmVhbF8yNDYuanNvboAAdHJldmVhbF81NC5qc29ugAB8cmV2ZWFsXzM3NC5qc29ugACEcmV2ZWFsXzEwMTIuanNvboAIBIACZAJoCASAAnwCgAgEgAJsAnAIBIACdAJ4AIRyZXZlYWxfMTAwOC5qc29ugACEcmV2ZWFsXzEwMzIuanNvboAAfHJldmVhbF81MjQuanNvboAAfHJldmVhbF85OTYuanNvboAIBIAChAKICASAAowCkAB8cmV2ZWFsXzk4My5qc29ugACEcmV2ZWFsXzExMTAuanNvboAAfHJldmVhbF82MDIuanNvboAAfHJldmVhbF82MDMuanNvboAIBIACnAKgCASAAxQDGAgEgAKkAqgIBIAC3ALgCASAAqwCsAgEgALEAsgIBIACtAK4CASAArwCwAB8cmV2ZWFsXzkwOS5qc29ugAB8cmV2ZWFsXzYwNS5qc29ugAB8cmV2ZWFsXzYwNi5qc29ugACEcmV2ZWFsXzEwMzcuanNvboAIBIACzALQCASAAtQC2AB8cmV2ZWFsXzYwOC5qc29ugAB8cmV2ZWFsXzk2My5qc29ugACEcmV2ZWFsXzEwMDUuanNvboAAhHJldmVhbF8xMTAyLmpzb26ACASAAuQC6AgEgAL8AwAIBIAC7ALwCASAAvQC+AB8cmV2ZWFsXzYxMi5qc29ugAB8cmV2ZWFsXzYxMy5qc29ugAB8cmV2ZWFsXzkxOS5qc29ugAB8cmV2ZWFsXzYxNS5qc29ugAgEgAMEAwgIBIADDAMQAHxyZXZlYWxfODEzLmpzb26AAHxyZXZlYWxfOTMwLmpzb26AAIRyZXZlYWxfMTA2Ny5qc29ugAB8cmV2ZWFsXzYxOS5qc29ugAgEgAMcAyAIBIADVANYCASAAyQDKAgEgAM8A0AIBIADLAMwCASAAzQDOAB8cmV2ZWFsXzk4OC5qc29ugAB8cmV2ZWFsXzYyMS5qc29ugAB8cmV2ZWFsXzYyMi5qc29ugACEcmV2ZWFsXzExMDcuanNvboAIBIADRANICASAA0wDUACEcmV2ZWFsXzEwODIuanNvboAAfHJldmVhbF84NzYuanNvboAAfHJldmVhbF82MjYuanNvboAAfHJldmVhbF82MjcuanNvboAIBIADXANgCASAA3QDeAgEgANkA2gIBIADbANwAHxyZXZlYWxfODQwLmpzb26AAIRyZXZlYWxfMTA4Ni5qc29ugACEcmV2ZWFsXzEwMzUuanNvboAAfHJldmVhbF82MzEuanNvboAIBIADfAOACASAA4QDiACEcmV2ZWFsXzEwNzAuanNvboAAfHJldmVhbF82MzMuanNvboAAfHJldmVhbF82MzQuanNvboAAfHJldmVhbF85NTEuanNvboAIBIADlAOYCASABAwEEAgEgAOcA6AIBIAD1APYCASAA6QDqAgEgAO8A8AIBIADrAOwCASAA7QDuAB8cmV2ZWFsXzg4My5qc29ugACEcmV2ZWFsXzEwMzEuanNvboAAhHJldmVhbF8xMDM5Lmpzb26AAHxyZXZlYWxfOTcwLmpzb26ACASAA8QDyAgEgAPMA9AAfHJldmVhbF85NjYuanNvboAAfHJldmVhbF82NDEuanNvboAAfHJldmVhbF82NDIuanNvboAAfHJldmVhbF82NDMuanNvboAIBIAD3APgCASAA/QD+AgEgAPkA+gIBIAD7APwAHxyZXZlYWxfOTM0Lmpzb26AAHxyZXZlYWxfNjQ1Lmpzb26AAHxyZXZlYWxfNjQ2Lmpzb26AAIRyZXZlYWxfMTA1Ny5qc29ugAgEgAP8BAAIBIAEBAQIAIRyZXZlYWxfMTA4Ny5qc29ugAB8cmV2ZWFsXzg1Mi5qc29ugAB8cmV2ZWFsXzk1Ny5qc29ugAB8cmV2ZWFsXzY1MS5qc29ugAgEgAQUBBgIBIAETARQCASABBwEIAgEgAQ0BDgIBIAEJAQoCASABCwEMAB8cmV2ZWFsXzkwOC5qc29ugAB8cmV2ZWFsXzY1My5qc29ugAB8cmV2ZWFsXzY1NC5qc29ugAB8cmV2ZWFsXzY1NS5qc29ugAgEgAQ8BEAIBIAERARIAHxyZXZlYWxfOTExLmpzb26AAHxyZXZlYWxfNjU3Lmpzb26AAHxyZXZlYWxfNjU4Lmpzb26AAHxyZXZlYWxfNjU5Lmpzb26ACASABFQEWAgEgARsBHAIBIAEXARgCASABGQEaACEcmV2ZWFsXzEwNTYuanNvboAAfHJldmVhbF84OTguanNvboAAfHJldmVhbF82NjIuanNvboAAfHJldmVhbF84NzguanNvboAIBIAEdAR4CASABHwEgAB8cmV2ZWFsXzg4OC5qc29ugAB8cmV2ZWFsXzY2NS5qc29ugAB8cmV2ZWFsXzgzMC5qc29ugAB8cmV2ZWFsXzk1My5qc29ugAgEgASMBJAIBIAFBAUICASABJQEmAgEgATMBNAIBIAEnASgCASABLQEuAgEgASkBKgIBIAErASwAHxyZXZlYWxfNjY4Lmpzb26AAHxyZXZlYWxfOTAwLmpzb26AAHxyZXZlYWxfNjcwLmpzb26AAHxyZXZlYWxfNjcxLmpzb26ACASABLwEwAgEgATEBMgAhHJldmVhbF8xMDUzLmpzb26AAHxyZXZlYWxfNjczLmpzb26AAIRyZXZlYWxfMTA2NC5qc29ugAB8cmV2ZWFsXzY3NS5qc29ugAgEgATUBNgIBIAE7ATwCASABNwE4AgEgATkBOgAfHJldmVhbF84ODEuanNvboAAfHJldmVhbF82NzcuanNvboAAfHJldmVhbF82NzguanNvboAAfHJldmVhbF82NzkuanNvboAIBIAE9AT4CASABPwFAACEcmV2ZWFsXzEwMTcuanNvboAAhHJldmVhbF8xMDAwLmpzb26AAHxyZXZlYWxfNjgyLmpzb26AAHxyZXZlYWxfNjgzLmpzb26ACASABQwFEAgEgAVEBUgIBIAFFAUYCASABSwFMAgEgAUcBSAIBIAFJAUoAHxyZXZlYWxfNjg0Lmpzb26AAHxyZXZlYWxfOTk5Lmpzb26AAHxyZXZlYWxfODQ5Lmpzb26AAHxyZXZlYWxfODYzLmpzb26ACASABTQFOAgEgAU8BUAAfHJldmVhbF82ODguanNvboAAfHJldmVhbF82ODkuanNvboAAfHJldmVhbF85NjguanNvboAAhHJldmVhbF8xMDE5Lmpzb26ACASABUwFUAgEgAVkBWgIBIAFVAVYCASABVwFYAB8cmV2ZWFsXzY5Mi5qc29ugACEcmV2ZWFsXzEwMjEuanNvboAAfHJldmVhbF82OTQuanNvboAAfHJldmVhbF84MjguanNvboAIBIAFbAVwCASABXQFeAB8cmV2ZWFsXzY5Ni5qc29ugAB8cmV2ZWFsXzgzMS5qc29ugAB8cmV2ZWFsXzY5OC5qc29ugAB8cmV2ZWFsXzY5OS5qc29ugAgEgAWEBYgIBIAF/AYACASABYwFkAgEgAXEBcgIBIAFlAWYCASABawFsAgEgAWcBaAIBIAFpAWoAHxyZXZlYWxfNzAwLmpzb26AAIRyZXZlYWxfMTA3Ni5qc29ugACEcmV2ZWFsXzEwODMuanNvboAAfHJldmVhbF83MDMuanNvboAIBIAFtAW4CASABbwFwACEcmV2ZWFsXzExMDguanNvboAAfHJldmVhbF84NDYuanNvboAAfHJldmVhbF84OTUuanNvboAAfHJldmVhbF85NDcuanNvboAIBIAFzAXQCASABeQF6AgEgAXUBdgIBIAF3AXgAHxyZXZlYWxfNzA4Lmpzb26AAHxyZXZlYWxfNzA5Lmpzb26AAHxyZXZlYWxfOTQ0Lmpzb26AAHxyZXZlYWxfNzExLmpzb26ACASABewF8AgEgAX0BfgAfHJldmVhbF85MzUuanNvboAAfHJldmVhbF83MTMuanNvboAAfHJldmVhbF84NTUuanNvboAAhHJldmVhbF8xMDYwLmpzb26ACASABgQGCAgEgAY8BkAIBIAGDAYQCASABiQGKAgEgAYUBhgIBIAGHAYgAHxyZXZlYWxfNzE2Lmpzb26AAHxyZXZlYWxfNzE3Lmpzb26AAHxyZXZlYWxfNzE4Lmpzb26AAHxyZXZlYWxfODY3Lmpzb26ACASABiwGMAgEgAY0BjgAhHJldmVhbF8xMDQyLmpzb26AAHxyZXZlYWxfOTYwLmpzb26AAHxyZXZlYWxfOTMyLmpzb26AAHxyZXZlYWxfNzIzLmpzb26ACASABkQGSAgEgAZcBmAIBIAGTAZQCASABlQGWAB8cmV2ZWFsXzcyNC5qc29ugAB8cmV2ZWFsXzcyNS5qc29ugAB8cmV2ZWFsXzkyNy5qc29ugACEcmV2ZWFsXzEwNzEuanNvboAIBIAGZAZoCASABmwGcAB8cmV2ZWFsXzcyOC5qc29ugAB8cmV2ZWFsXzk3Ni5qc29ugAB8cmV2ZWFsXzkxOC5qc29ugACEcmV2ZWFsXzEwNzQuanNvboAIBIAGfAaACASABvQG+AgEgAaEBogIBIAGvAbACASABowGkAgEgAakBqgIBIAGlAaYCASABpwGoAB8cmV2ZWFsXzg0NS5qc29ugAB8cmV2ZWFsXzczMy5qc29ugAB8cmV2ZWFsXzk4NC5qc29ugAB8cmV2ZWFsXzczNS5qc29ugAgEgAasBrAIBIAGtAa4AHxyZXZlYWxfNzM2Lmpzb26AAHxyZXZlYWxfODk2Lmpzb26AAHxyZXZlYWxfOTcyLmpzb26AAHxyZXZlYWxfNzM5Lmpzb26ACASABsQGyAgEgAbcBuAIBIAGzAbQCASABtQG2AB8cmV2ZWFsXzc0MC5qc29ugAB8cmV2ZWFsXzc0MS5qc29ugACEcmV2ZWFsXzEwMDMuanNvboAAfHJldmVhbF84MzUuanNvboAIBIAG5AboCASABuwG8AB8cmV2ZWFsXzc0NC5qc29ugAB8cmV2ZWFsXzgyNC5qc29ugACEcmV2ZWFsXzEwMTYuanNvboAAfHJldmVhbF85ODUuanNvboAIBIAG/AcACASABzQHOAgEgAcEBwgIBIAHHAcgCASABwwHEAgEgAcUBxgAfHJldmVhbF83NDguanNvboAAfHJldmVhbF84MzYuanNvboAAfHJldmVhbF84OTcuanNvboAAhHJldmVhbF8xMDM4Lmpzb26ACASAByQHKAgEgAcsBzAAfHJldmVhbF85OTAuanNvboAAfHJldmVhbF83NTMuanNvboAAfHJldmVhbF83NTQuanNvboAAfHJldmVhbF85MjguanNvboAIBIAHPAdACASAB1QHWAgEgAdEB0gIBIAHTAdQAHxyZXZlYWxfNzU2Lmpzb26AAHxyZXZlYWxfNzU3Lmpzb26AAHxyZXZlYWxfNzU4Lmpzb26AAHxyZXZlYWxfNzU5Lmpzb26ACASAB1wHYAgEgAdkB2gAfHJldmVhbF84OTQuanNvboAAfHJldmVhbF83NjEuanNvboAAfHJldmVhbF85NDMuanNvboAAhHJldmVhbF8xMDg0Lmpzb26ACASAB3QHeAgEgAfsB/AIBIAHfAeACASAB7QHuAgEgAeEB4gIBIAHnAegCASAB4wHkAgEgAeUB5gAfHJldmVhbF83NjQuanNvboAAfHJldmVhbF84NDMuanNvboAAfHJldmVhbF85MjMuanNvboAAfHJldmVhbF85MTMuanNvboAIBIAHpAeoCASAB6wHsACEcmV2ZWFsXzEwMDkuanNvboAAfHJldmVhbF83NjkuanNvboAAhHJldmVhbF8xMDI5Lmpzb26AAHxyZXZlYWxfOTM3Lmpzb26ACASAB7wHwAgEgAfUB9gIBIAHxAfICASAB8wH0AB8cmV2ZWFsXzc3Mi5qc29ugAB8cmV2ZWFsXzc3My5qc29ugACEcmV2ZWFsXzEwNzkuanNvboAAhHJldmVhbF8xMDU5Lmpzb26ACASAB9wH4AgEgAfkB+gAfHJldmVhbF83NzYuanNvboAAfHJldmVhbF84NjEuanNvboAAhHJldmVhbF8xMDEwLmpzb26AAHxyZXZlYWxfNzc5Lmpzb26ACASAB/QH+AgEgAgsCDAIBIAH/AgACASACBQIGAgEgAgECAgIBIAIDAgQAIRyZXZlYWxfMTA4MS5qc29ugAB8cmV2ZWFsXzgwOS5qc29ugAB8cmV2ZWFsXzc4Mi5qc29ugAB8cmV2ZWFsXzk0Ni5qc29ugAgEgAgcCCAIBIAIJAgoAHxyZXZlYWxfNzg0Lmpzb26AAHxyZXZlYWxfODQ0Lmpzb26AAHxyZXZlYWxfNzg2Lmpzb26AAHxyZXZlYWxfNzg3Lmpzb26ACASACDQIOAgEgAhMCFAIBIAIPAhACASACEQISAB8cmV2ZWFsXzc4OC5qc29ugAB8cmV2ZWFsXzc4OS5qc29ugAB8cmV2ZWFsXzc5MC5qc29ugAB8cmV2ZWFsXzc5MS5qc29ugAgEgAhUCFgIBIAIXAhgAHxyZXZlYWxfOTkxLmpzb26AAHxyZXZlYWxfODEyLmpzb26AAHxyZXZlYWxfOTAyLmpzb26AAHxyZXZlYWxfNzk1Lmpzb26B6jDk7"


def test_vm_dict_from_boc():
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,
            56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
            83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107,
            108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128,
            129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149,
            150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170,
            171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
            192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
            213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233,
            234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254,
            255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268]

    values = ['reveal_822.json', 'reveal_841.json', 'reveal_331.json', 'reveal_230.json', 'reveal_572.json',
              'reveal_569.json', 'reveal_1013.json', 'reveal_1094.json', 'reveal_1077.json', 'reveal_329.json',
              'reveal_915.json', 'reveal_979.json', 'reveal_13.json', 'reveal_816.json', 'reveal_591.json',
              'reveal_458.json', 'reveal_273.json', 'reveal_533.json', 'reveal_202.json', 'reveal_954.json',
              'reveal_1092.json', 'reveal_1025.json', 'reveal_526.json', 'reveal_939.json', 'reveal_811.json',
              'reveal_858.json', 'reveal_141.json', 'reveal_556.json', 'reveal_921.json', 'reveal_338.json',
              'reveal_893.json', 'reveal_86.json', 'reveal_33.json', 'reveal_891.json', 'reveal_579.json',
              'reveal_926.json', 'reveal_147.json', 'reveal_379.json', 'reveal_916.json', 'reveal_981.json',
              'reveal_1050.json', 'reveal_810.json', 'reveal_434.json', 'reveal_1051.json', 'reveal_950.json',
              'reveal_987.json', 'reveal_257.json', 'reveal_864.json', 'reveal_940.json', 'reveal_95.json',
              'reveal_920.json', 'reveal_1109.json', 'reveal_246.json', 'reveal_54.json', 'reveal_374.json',
              'reveal_1012.json', 'reveal_1008.json', 'reveal_1032.json', 'reveal_524.json', 'reveal_996.json',
              'reveal_983.json', 'reveal_1110.json', 'reveal_602.json', 'reveal_603.json', 'reveal_909.json',
              'reveal_605.json', 'reveal_606.json', 'reveal_1037.json', 'reveal_608.json', 'reveal_963.json',
              'reveal_1005.json', 'reveal_1102.json', 'reveal_612.json', 'reveal_613.json', 'reveal_919.json',
              'reveal_615.json', 'reveal_813.json', 'reveal_930.json', 'reveal_1067.json', 'reveal_619.json',
              'reveal_988.json', 'reveal_621.json', 'reveal_622.json', 'reveal_1107.json', 'reveal_1082.json',
              'reveal_876.json', 'reveal_626.json', 'reveal_627.json', 'reveal_840.json', 'reveal_1086.json',
              'reveal_1035.json', 'reveal_631.json', 'reveal_1070.json', 'reveal_633.json', 'reveal_634.json',
              'reveal_951.json', 'reveal_883.json', 'reveal_1031.json', 'reveal_1039.json', 'reveal_970.json',
              'reveal_966.json', 'reveal_641.json', 'reveal_642.json', 'reveal_643.json', 'reveal_934.json',
              'reveal_645.json', 'reveal_646.json', 'reveal_1057.json', 'reveal_1087.json', 'reveal_852.json',
              'reveal_957.json', 'reveal_651.json', 'reveal_908.json', 'reveal_653.json', 'reveal_654.json',
              'reveal_655.json', 'reveal_911.json', 'reveal_657.json', 'reveal_658.json', 'reveal_659.json',
              'reveal_1056.json', 'reveal_898.json', 'reveal_662.json', 'reveal_878.json', 'reveal_888.json',
              'reveal_665.json', 'reveal_830.json', 'reveal_953.json', 'reveal_668.json', 'reveal_900.json',
              'reveal_670.json', 'reveal_671.json', 'reveal_1053.json', 'reveal_673.json', 'reveal_1064.json',
              'reveal_675.json', 'reveal_881.json', 'reveal_677.json', 'reveal_678.json', 'reveal_679.json',
              'reveal_1017.json', 'reveal_1000.json', 'reveal_682.json', 'reveal_683.json', 'reveal_684.json',
              'reveal_999.json', 'reveal_849.json', 'reveal_863.json', 'reveal_688.json', 'reveal_689.json',
              'reveal_968.json', 'reveal_1019.json', 'reveal_692.json', 'reveal_1021.json', 'reveal_694.json',
              'reveal_828.json', 'reveal_696.json', 'reveal_831.json', 'reveal_698.json', 'reveal_699.json',
              'reveal_700.json', 'reveal_1076.json', 'reveal_1083.json', 'reveal_703.json', 'reveal_1108.json',
              'reveal_846.json', 'reveal_895.json', 'reveal_947.json', 'reveal_708.json', 'reveal_709.json',
              'reveal_944.json', 'reveal_711.json', 'reveal_935.json', 'reveal_713.json', 'reveal_855.json',
              'reveal_1060.json', 'reveal_716.json', 'reveal_717.json', 'reveal_718.json', 'reveal_867.json',
              'reveal_1042.json', 'reveal_960.json', 'reveal_932.json', 'reveal_723.json', 'reveal_724.json',
              'reveal_725.json', 'reveal_927.json', 'reveal_1071.json', 'reveal_728.json', 'reveal_976.json',
              'reveal_918.json', 'reveal_1074.json', 'reveal_845.json', 'reveal_733.json', 'reveal_984.json',
              'reveal_735.json', 'reveal_736.json', 'reveal_896.json', 'reveal_972.json', 'reveal_739.json',
              'reveal_740.json', 'reveal_741.json', 'reveal_1003.json', 'reveal_835.json', 'reveal_744.json',
              'reveal_824.json', 'reveal_1016.json', 'reveal_985.json', 'reveal_748.json', 'reveal_836.json',
              'reveal_897.json', 'reveal_1038.json', 'reveal_990.json', 'reveal_753.json', 'reveal_754.json',
              'reveal_928.json', 'reveal_756.json', 'reveal_757.json', 'reveal_758.json', 'reveal_759.json',
              'reveal_894.json', 'reveal_761.json', 'reveal_943.json', 'reveal_1084.json', 'reveal_764.json',
              'reveal_843.json', 'reveal_923.json', 'reveal_913.json', 'reveal_1009.json', 'reveal_769.json',
              'reveal_1029.json', 'reveal_937.json', 'reveal_772.json', 'reveal_773.json', 'reveal_1079.json',
              'reveal_1059.json', 'reveal_776.json', 'reveal_861.json', 'reveal_1010.json', 'reveal_779.json',
              'reveal_1081.json', 'reveal_809.json', 'reveal_782.json', 'reveal_946.json', 'reveal_784.json',
              'reveal_844.json', 'reveal_786.json', 'reveal_787.json', 'reveal_788.json', 'reveal_789.json',
              'reveal_790.json', 'reveal_791.json', 'reveal_991.json', 'reveal_812.json', 'reveal_902.json',
              'reveal_795.json', 'reveal_796.json', 'reveal_797.json', 'reveal_798.json', 'reveal_912.json',
              'reveal_901.json', 'reveal_801.json', 'reveal_802.json', 'reveal_803.json', 'reveal_804.json',
              'reveal_1106.json', 'reveal_806.json', 'reveal_833.json', 'reveal_808.json']

    d = VmDict(64, cell_root=reveal_dict_boc)

    for i, x in enumerate(d):
        assert x[0] == keys[i]
        assert x[1].load_string() == values[i]

    d = VmDict(64, cell_root=CellSlice(reveal_dict_boc))

    for i, x in enumerate(d):
        assert x[0] == keys[i]
        assert x[1].load_string() == values[i]

    d = VmDict(64, cell_root=Cell(reveal_dict_boc))

    for i, x in enumerate(d):
        assert x[0] == keys[i]
        assert x[1].load_string() == values[i]


def test_vm_dict_not_signed():
    for my_key in [int("1" * 64, 2), 0, 179, 57, 228]:
        d = VmDict(64)
        assert d.is_empty() is True

        my_value = CellBuilder().store_uint(32, 32).begin_parse()

        my_hash = my_value.get_hash()
        d.set(my_key, my_value)

        key_stored, value_stored = d.get_minmax_key()
        assert key_stored == my_key
        assert value_stored.get_hash() == my_hash

        from_dict = d.lookup(my_key)
        assert from_dict.get_hash() == my_hash

    with pytest.raises(ValueError):
        d = VmDict(64)
        d.set(-1, CellBuilder().begin_parse())


def test_vm_dict_signed():
    for sign in [1, -1]:
        for my_key in [int("1" * 63, 2), 0, 179, 57, 228]:
            my_key = sign * my_key

            d = VmDict(64, True)
            assert d.is_empty() is True

            my_value = CellBuilder().store_uint(32, 32).begin_parse()

            my_hash = my_value.get_hash()
            d.set(my_key, my_value)

            key_stored, value_stored = d.get_minmax_key()
            assert key_stored == my_key
            assert value_stored.get_hash() == my_hash

            from_dict = d.lookup(my_key)
            assert from_dict.get_hash() == my_hash


def test_vm_dict_large():
    d = VmDict(257, True)

    cb = CellBuilder()
    main_cell = CellBuilder()
    cell = main_cell
    for i in range(100):
        cur_cell = CellBuilder()
        cur_cell.store_bitstring("1" * 1023)
        cell.store_ref(cur_cell.end_cell())
        cell = cur_cell

    main_cell = main_cell.end_cell()
    cb.store_ref(main_cell)
    cs = cb.begin_parse()

    for i in range(10000):
        d.set(i, cs)

    d.set(-1 * int("1" * 256, 2), cs)

    cc_val = d.lookup(-1 * int("1" * 256, 2))
    assert cc_val.get_hash() == cs.get_hash()


def test_vm_dict_set():
    d = VmDict(32)

    # set(self, key: int, value: CellSlice, mode: str = "set", key_len: int = 0, signed: bool = None)
    e = CellBuilder().begin_parse()

    # Large value for test
    cb = CellBuilder()
    main_cell = CellBuilder()
    cell = main_cell
    for i in range(100):
        cur_cell = CellBuilder()
        cur_cell.store_bitstring("1" * 1023)
        cell.store_ref(cur_cell.end_cell())
        cell = cur_cell

    main_cell = main_cell.end_cell()
    cb.store_ref(main_cell)
    cs = cb.begin_parse()

    d.set(0, e, mode="replace")

    # Will not set, because no value already
    with pytest.raises(RuntimeError):
        d.get_minmax_key()

    # Test set with mode=add
    d.set(0, e, mode="add")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == e.get_hash()

    # Will not update because already have value
    d.set(0, cs, mode="add")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == e.get_hash()

    d.set(0, cs, mode="replace")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == cs.get_hash()

    d.set(0, e, mode="set")

    key, value = d.get_minmax_key()
    assert key == 0
    assert value.get_hash() == e.get_hash()

    # Force signed
    d.set(-123, cs, signed=True)

    assert d.lookup(4294967173).get_hash() == cs.get_hash()
    assert d.lookup(-123, signed=True).get_hash() == cs.get_hash()


def test_not_valid():
    with pytest.raises(AssertionError):
        d = VmDict(2)
        d.set(100, CellBuilder().begin_parse())


def test_empty():
    d = VmDict(32)
    assert d.is_empty() is True

    d = VmDict(32)
    d.set(0, CellBuilder().begin_parse())
    assert d.is_empty() is False

    d.lookup_delete(0)
    assert d.is_empty() is True


def test_get_cell():
    d = VmDict(64, cell_root=reveal_dict_boc)
    c = d.get_cell()

    assert isinstance(c, Cell)
    assert c.to_boc() == reveal_dict_boc


def test_lookup_nearest():
    d = VmDict(64)

    for i in range(100):
        d.set(i, CellBuilder().store_uint(i, 64).begin_parse())

    def _f(key, **kwargs):
        key, value = d.lookup_nearest_key(key, **kwargs)
        assert value.load_uint(64) == key
        return key

    for i in range(1, 99):
        assert _f(i) == i + 1
        assert _f(i, fetch_next=False) == i - 1

    with pytest.raises(RuntimeError):
        # Can't load prev value
        _f(0, fetch_next=False)

    with pytest.raises(RuntimeError):
        # Can't load next value
        _f(100)

    d = VmDict(64, signed=True)
    d.set(8, CellBuilder().begin_parse())
    d.set(6, CellBuilder().begin_parse())
    d.set(-1, CellBuilder().begin_parse())
    d.set(-2, CellBuilder().begin_parse())
    d.set(-3, CellBuilder().begin_parse())

    assert d.lookup_nearest_key(6)[0] == 8
    assert d.lookup_nearest_key(-3)[0] == -2
    assert d.lookup_nearest_key(-1, False)[0] == -2
    assert d.lookup_nearest_key(6, False)[0] == -1

    # TODO: tests on invert_first


def test_get_minmax():
    d = VmDict(64, signed=True)
    d.set(8, CellBuilder().begin_parse())
    d.set(6, CellBuilder().begin_parse())
    d.set(-1, CellBuilder().begin_parse())
    d.set(-2, CellBuilder().begin_parse())
    d.set(-3, CellBuilder().begin_parse())

    assert d.get_minmax_key()[0] == 8 and isinstance(d.get_minmax_key()[1], CellSlice)
    assert d.get_minmax_key(invert_first=False)[0] == -1 and isinstance(d.get_minmax_key(invert_first=False)[1],
                                                                        CellSlice)
    assert d.get_minmax_key(False)[0] == -3 and isinstance(d.get_minmax_key(False)[1], CellSlice)
    assert d.get_minmax_key(False, False)[0] == 6 and isinstance(d.get_minmax_key(False, False)[1], CellSlice)


def test_set_ref():
    d = VmDict(64)

    for i in range(1000):
        d.set_ref(i, CellBuilder().store_uint(i, 64).end_cell())

    for i in range(1000):
        c = d.lookup_ref(i)
        assert isinstance(c, Cell)
        assert c.begin_parse().load_uint(64) == i

    d = VmDict(64, True)

    for i in range(-1000, 1000):
        d.set_ref(i, CellBuilder().store_int(i, 64).end_cell())

    for i in range(-1000, 1000):
        c = d.lookup_ref(i)
        assert isinstance(c, Cell)
        assert c.begin_parse().load_int(64) == i


def test_set_builder():
    d = VmDict(64)

    for i in range(1000):
        d.set_builder(i, CellBuilder().store_uint(i, 64) \
                      .store_ref(CellBuilder().store_uint(i, 64).end_cell()))

    for i in range(1000):
        c = d.lookup(i)
        assert isinstance(c, CellSlice)
        assert c.load_uint(64) == i
        assert c.refs == 1

    d = VmDict(64, True)

    for i in range(-1000, 1000):
        d.set_builder(i, CellBuilder().store_int(i, 64) \
                      .store_ref(CellBuilder().store_int(i, 64).end_cell()))

    for i in range(-1000, 1000):
        c = d.lookup(i)
        assert isinstance(c, CellSlice)
        assert c.load_int(64) == i
        assert c.refs == 1


def test_lookup_delete():
    d = VmDict(64)

    for i in range(5000):
        d.set_builder(i, CellBuilder().store_uint(i, 64))

    total = 0
    for _ in d:
        total += 1

    assert total == 5000

    for i in range(4999):
        cs = d.lookup_delete(i)
        assert cs.load_uint(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 1

    d = VmDict(64, True)

    for i in range(-5000, 5000):
        d.set_builder(i, CellBuilder().store_int(i, 64))

    total = 0
    for _ in d:
        total += 1

    assert total == 10000

    for i in range(-4999, 4999):
        cs = d.lookup_delete(i)
        assert cs.load_int(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 2


def test_lookup_ref():
    d = VmDict(64)

    for i in range(5000):
        d.set_ref(i, CellBuilder().store_uint(i, 64).end_cell())

    total = 0
    for _ in d:
        total += 1

    assert total == 5000

    for i in range(5000):
        c = d.lookup_ref(i).begin_parse()
        assert c.load_uint(64) == i

    for i in range(4999):
        cs = d.lookup_delete_ref(i).begin_parse()
        assert cs.load_uint(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 1

    d = VmDict(64, True)

    for i in range(-5000, 5000):
        d.set_ref(i, CellBuilder().store_int(i, 64).end_cell())

    total = 0
    for _ in d:
        total += 1

    assert total == 10000

    for i in range(-5000, 5000):
        cs = d.lookup_ref(i).begin_parse()
        assert cs.load_int(64) == i

    for i in range(-4999, 4999):
        cs = d.lookup_delete_ref(i).begin_parse()
        assert cs.load_int(64) == i

    total = 0
    for _ in d:
        total += 1

    assert total == 2


def test_set_get_item():
    d = VmDict(256)

    test_builder = CellBuilder().store_uint(0, 64).store_ref(CellBuilder().store_uint(1, 64).end_cell())
    d[1] = test_builder
    d["test"] = test_builder
    d["oh my god"] = CellBuilder().begin_parse()
    d["test2"] = test_builder.end_cell()

    cs = d[1]
    assert cs.load_uint(64) == 0
    assert cs.load_ref(as_cs=True).load_uint(64) == 1

    cs = d["test"]
    assert cs.load_uint(64) == 0
    assert cs.load_ref(as_cs=True).load_uint(64) == 1

    cs = d["oh my god"]
    assert cs.bits == 0
    assert cs.refs == 0

    cs = d["test2"].load_ref(as_cs=True)
    assert cs.load_uint(64) == 0
    assert cs.load_ref(as_cs=True).load_uint(64) == 1
