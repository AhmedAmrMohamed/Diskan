class Plotter:
    def __init__(self):
        self.init = False
        self.matplotlib_exists = self.imports()


    def plot(self, node):
            dirsize = node.getDirsPercentage()
            y = np.array(dirsize)
            plt.pie(y)
            plt.show()

    def imports(self):
        self.init = True
        try:
            global plt
            global np
            global matplotlib_exists
            import matplotlib
            import matplotlib.pyplot as plt
            import numpy as np
            return True
        except Exception as e:
            print(e)
            return False
                                                        
    