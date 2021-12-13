import random
import numpy as np

class MyDataset:
    def __init__(self,datas,batch_size,shuffle):
        self.datas = datas
        self.batch_size = batch_size
        self.shuffle = shuffle

    def __iter__(self): # 希望返回一个具有 __next__的对象
        return DataLoader(self)


    def __len__(self):
        return len(self.datas)


class DataLoader:
    def __init__(self,dataset):
        self.dataset = dataset
        self.batch_size = batch_size
        self.indexs = [i for i in range(len(self.dataset))]
        if dataset.shuffle:
            np.random.shuffle(self.indexs)
        self.cursor = 0

    def __next__(self):
        index = self.indexs[self.cursor:self.cursor + self.batch_size]
        data = self.dataset.datas[index]

        if self.cursor >= len(self.dataset):
            raise StopIteration

        self.cursor += self.batch_size
        return data


if __name__ == "__main__":
    datas = np.arange(10)
    shuffle = True
    batch_size = 3
    dataset = MyDataset(datas,batch_size,shuffle)

    for i in dataset:  # 1.去dataset中获取一个具有__next__的对象   2. 从这个对象中依次取数据  3. 到什么时候结束?
        print(i)





