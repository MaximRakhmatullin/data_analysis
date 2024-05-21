class MatrixAnalysis:
    @staticmethod
    def sum(matrix: list[list[int]]) -> int:
        sum_number = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                sum_number += matrix[i][j]
        return sum_number

    @staticmethod
    def max(matrix: list[list[int]]) -> int:
        max_number = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] > max_number:
                    max_number = matrix[i][j]
        return max_number

    @staticmethod
    def min(matrix: list[list[int]]) -> int:
        min_number = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] < min_number:
                    min_number = matrix[i][j]
        return min_number

    @staticmethod
    def mode(matrix: list[list[int]]) -> int:
        if len(matrix) == 0:
            return 0

        number_frequency = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                number = matrix[i][j]
                if number in number_frequency:
                    number_frequency[number] += 1
                else:
                    number_frequency[number] = 1

        frequent_number = matrix[0][0]
        max_frequency = 0
        for key in number_frequency:
            if number_frequency[key] > max_frequency:
                max_frequency = number_frequency[key]
                frequent_number = key

        return frequent_number
