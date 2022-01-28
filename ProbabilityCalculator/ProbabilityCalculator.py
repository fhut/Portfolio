import random
import copy
random.seed()

class Hat:

    def __init__(self, **kwargs):

        self.contents = []


        for ball, count in kwargs.items():
            self.contents += [ball] * count

        self.num_of_balls = len(self.contents)



    def draw(self, draw_from_hat):

        len_contents = len(self.contents)

        if draw_from_hat > len_contents:
            return self.contents

        balls_removed = []

        for i in range(draw_from_hat):

            ball_to_remove = random.randint(1, len_contents -1)
            balls_removed.append(self.contents.pop(ball_to_remove))
            len_contents -= 1

        return balls_removed





def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    count = 0

    for i in range(num_experiments):



        hat_copy = copy.deepcopy(hat)

        balls = hat_copy.draw(num_balls_drawn)

        ball_counts = {}




        for each in balls:
            ball_count_accumulator = ball_counts.get(each, 0)
            ball_counts[each] = ball_count_accumulator + 1




        match = True

        for ball, total in expected_balls.items():
            if ball_counts.get(ball, 0) < total:
                match = False
                break



        if match:
            count += 1



    return count / num_experiments






balls = {"blue":2,"green":1}

hat = Hat(red = 3, blue = 5)



print(experiment(hat, balls, 4, 1000))



