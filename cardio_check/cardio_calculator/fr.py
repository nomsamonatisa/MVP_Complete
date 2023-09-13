class Framingham:

    def __init__(self, gender, age, diabetes, smoker, blood_pressure, total_cholesterol, hdl, treated_blood_pressure):
         # Initialize the Framingham class with various health parameters
        self.gender = gender
        self.age = age
        self.diabetes = diabetes
        self.smoker = smoker
        self.blood_pressure = blood_pressure
        self.total_cholesterol = total_cholesterol
        self.hdl = hdl
        self.treated_blood_pressure = treated_blood_pressure

    def calculate_risk_score(self, age_range, cholesterol_range, hdl_range, blood_pressure_ranges, risk_factors):
         # Calculate the Framingham risk score based on provided health parameters and risk factor ranges
        risk_score = 0

        # Calculate risk score based on age within specified age ranges
        if age_range:
            for start, end, score in age_range:
                if start < self.age <= end:
                    risk_score += score

        # Add additional risk based on diabetes and smoking status
        risk_score += self.diabetes * risk_factors['diabetes']
        risk_score += self.smoker * risk_factors['smoker']

        # Adjust risk score based on treated or untreated blood pressure and blood pressure ranges
        if self.treated_blood_pressure == 0:  # BP Treated
            for start, end, score in blood_pressure_ranges:
                if start < self.blood_pressure <= end:
                    risk_score += (score +2)

        if self.treated_blood_pressure == 1:  # BP Not Treated
            for start, end, score in blood_pressure_ranges:
                if start < self.blood_pressure <= end:
                    risk_score += score

        # Adjust risk score based on total cholesterol and HDL cholesterol levels
        for start, end, score in cholesterol_range:
            if start < self.total_cholesterol <= end:
                risk_score += score

        for start, end, score in hdl_range:
            if start < self.hdl <= end:
                risk_score += score

        return risk_score

    def calculate_score(self, risk_score, score_mapping):
        # Map the calculated risk score to a specific risk score category based on predefined score ranges

        for lower_bound, upper_bound, score in score_mapping:
            if lower_bound < risk_score <= upper_bound:
                return score
        return score_mapping[-1][2]  # Default max score if no range matches
    
    def calculate_risk_level(self, risk_score):
        # Determine the risk level based on gender-specific risk score mappings

        if self.gender == 0:
            risk_level_mapping = {
                (float('-inf'), 8.6): "Low Risk",
                (10.0, 18.51): "Medium Risk",
                (21.5, float('inf')): "High Risk"
            }
        else:
            risk_level_mapping = {
                (float('-inf'), 9.4): "Low Risk",
                (11.2, 18.4): "Medium Risk",
                (21.6, float('inf')): "High Risk"
            }

        for (lower, upper), level in risk_level_mapping.items():
            if lower <= risk_score <= upper:
                return level
        return "Unknown"
    

    def FraminghamRisk(self):
        # Calculate the overall Framingham risk by combining the individual risk factors and mapping to a risk level
        
        score_mapping_male = [(float('-inf'), -2, 1), (-2, -1, 1.1), (-1, 0, 1.4), (0, 1, 1.6), (1, 2, 1.9),
                              (2, 3, 2.3), (3, 4, 2.8), (4, 5, 3.3), (5, 6, 3.9), (6, 7, 4.7),
                              (7, 8, 5.6), (8, 9, 6.7), (9, 10, 7.9), (10, 11, 9.4), (11, 12, 11.2),
                              (12, 13, 13.3), (13, 14, 15.6), (14, 15, 18.4), (15, 16, 18.4),
                              (16, 17, 21.6), (17, 18, 25.3), (18, 19, 29.4), (19, 20, 30), (20, float('inf'), 30)]

        score_mapping_female = [(float('-inf'), -2, 1), (-2, -1, 1.2), (-1, 0, 1.5), (0, 1, 1.7), (1, 2, 2),
                                (2, 3, 2.4), (3, 4, 2.8), (4, 5, 3.3), (5, 6, 3.9), (6, 7, 4.5),
                                (7, 8, 5.3), (8, 9, 6.3), (9, 10, 7.3), (10, 11, 8.6), (11, 12, 10.0),
                                (12, 13, 11.7), (13, 14, 13.7), (14, 15, 15.9), (15, 16, 15.9),
                                (16, 17, 18.51), (17, 18, 21.5), (18, 19, 24.8), (19, 20, 27.5), (20, float('inf'), 30)]

        age_range_male = [(0, 34, 0), (34, 39, 2), (39, 44, 5), (44, 49, 7), (49, 54, 8),
                          (54, 59, 10), (59, 64, 11), (64, 69, 12), (69, 74, 14), (74, float('inf'), 15)]

        age_range_female = [(0, 34, 0), (34, 39, 2), (39, 44, 4), (44, 49, 5), (49, 54, 7),
                            (54, 59, 8), (59, 64, 9), (64, 69, 10), (69, 74, 11), (74, float('inf'), 12)]

        cholesterol_range_male = [(float('-inf'), 4.1, 0), (4.1, 5.19, 1), (5.19, 6.19, 2),
                             (6.19, 7.2, 3), (7.2, float('inf'), 4)]
        cholesterol_range_female = [(float('-inf'), 4.1, 0), (4.1, 5.19, 1), (5.19, 6.19, 3),
                             (6.19, 7.2, 4), (7.2, float('inf'), 5)]

        hdl_range = [(float('-inf'), 0.9, 2), (0.9, 1.19, 1), (1.19, 1.29, 0),
                     (1.29, 1.6, -1), (1.6, float('inf'), -2)]

        blood_pressure_ranges_male = [
            (float('-inf'), 120, -2), (120, 129, 0), (129, 139, 1),
            (139, 149, 2), (149, 159, 2), (159, float('inf'), 3)
        ]
        blood_pressure_ranges_female = [
            (float('-inf'), 120, -3), (120, 129, 0), (129, 139, 1),
            (139, 149, 2), (149, 159, 4), (159, float('inf'), 5)
        ]

        if self.gender == 0:
            age_range = age_range_male
            score_mapping = score_mapping_male
            cholesterol_range = cholesterol_range_male
            blood_pressure_ranges = blood_pressure_ranges_male
        else:
            age_range = age_range_female
            score_mapping = score_mapping_female
            cholesterol_range = cholesterol_range_female
            blood_pressure_ranges = blood_pressure_ranges_female

        risk_score = self.calculate_risk_score(age_range, cholesterol_range, hdl_range, blood_pressure_ranges,
                                               {'diabetes': 0 if self.diabetes == 0 else 4, 'smoker': 0 if self.smoker == 0 else 3})
        score = self.calculate_score(risk_score, score_mapping)
        risk_level = self.calculate_risk_level(risk_score)
        return float(score), risk_level


