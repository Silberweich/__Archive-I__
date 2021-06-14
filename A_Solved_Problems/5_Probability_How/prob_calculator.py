import copy
import random
# Consider using the modules imported above.

class Hat:
    # Attribute
    contents = list()
    temp_contents = list()
    #Constructor
    def __init__(self, **kwarg):
        self.contents.clear()
        self.temp_contents.clear()

        for key, value in kwarg.items():
            for n in range(0, value):
                self.contents.append(key)
        self.temp_contents = copy.deepcopy(self.contents)
        
        # print(self.contents)

    def draw(self, amount : int) -> list:
        ret_list = list()
        if amount >= len(self.contents):
            return self.contents
        else:
            for n in range(0, amount):
                ran_index = random.randint(0, len(self.contents) - 1)
                
                # print("INDEX", ran_index)
                # print("before", self.contents)
                ret_list.append(self.contents.pop(ran_index))
                # print("after", self.contents)
                # print("LIST", ret_list)
        return ret_list

    def reset(self):
        self.contents = copy.deepcopy(self.temp_contents)

    def __del__(self):
        self.contents.clear()
        self.temp_contents.clear()

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    FINAL_RATIO = float()
    success = int(0)
    drawn = list()
    expected_list = list()
    print(hat.contents)
    print(expected_balls)
    # change dict to list
    for key, value in expected_balls.items():
            for n in range(0, value):
                expected_list.append(key)
    print(expected_list)

    for i in range(0, num_experiments):
        drawn = hat.draw(num_balls_drawn)
        #print(drawn)
        if(check_if_equal(drawn, expected_list, expected_balls)):
            success += 1
        hat.reset()

    FINAL_RATIO = success / num_experiments

    return FINAL_RATIO

def check_if_equal(list_1_check, list_2_expect, dicta):
    boola = True

    for ball in list_2_expect:
        if ball in list_1_check:
            list_1_check.remove(ball)
        else:
            boola = False

    return boola