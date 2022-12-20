import chunk
from distutils.command.clean import clean


class Score():
    """
    A Class to generate scores

    Provides the following methods:

    """
    def clean(self, raw_data):
        """
        Works on raw_data to produce clean data of scores

        Returns: A dictionary of scores
        rtype: Dict

        Example output:
        [
            {'You': 'Wordle 317 5/6'},
            {'Manohar Nanaba': 'Wordle 322 4/6'},
            {'You': 'Wordle 322 5/6'},
            {'Manohar Nanaba': 'Wordle 319 4/6'}
        ]
        """
        match = ("You", "Manohar", "Wordle")
        data = [item.replace(":","").replace("\n","") for item in raw_data if item.startswith(match)]
        clean_data = ["placeholder"]

        for item in data:
            if clean_data[-1] != item:
                clean_data.append(item)

        scores=[]
        for i in range(len(clean_data)):
            if i == len(clean_data) - 1:
                break
            if clean_data[i].startswith(("You","Manohar")):
                score = {clean_data[i]:clean_data[i+1]}
                if score[clean_data[i]].startswith("Wordle"):
                    scores.append(score)

        return scores

    def points(self, game, scores):
        """
        Returns the points earned of individuals for a given game

        Parameters: game
        Type: integer

        Returns: points earned by each individual for that game
        Type : dict

        Example Output:
        {
            "Yadhu" : 3,
            "Manohar" : 5
        }
        """
        points_for_game = {}
        for score in scores:
            if 'You' in score and str(game) in score['You']:
                points_for_game["Yadhu"] = self.calculate(score['You'])
            if 'Manohar Nanaba' in score and str(game) in score['Manohar Nanaba']:
                points_for_game["Manohar"] = self.calculate(score['Manohar Nanaba'])

        return points_for_game

    
    def calculate(self, wordle_string):
        """
        Calculates the points earned based on the Wordle string

        Parameter: Wordle string ( such as 'Wordle 322 5/6' or 'Wordle 318 X/6')
        Type: string

        Returns: points
        Type: integer
        """
        score = wordle_string.split(' ')[2]

        legend = {
            "1/6" : 6,
            "2/6" : 4,
            "3/6" : 3,
            "4/6" : 2,
            "5/6" : 1,
            "6/6" : 0,
            "X/6" : -2
        }

        points = legend[score]
        return points
