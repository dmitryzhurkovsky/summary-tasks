"""Task3"""
from flask import Flask, jsonify, request

app = Flask(__name__)
client = app.test_client()


def appearance(input_data):
    """Count total time of attendance at the lesson of students and teachers."""
    lesson_timestep = set()
    tutor_timestep = set()
    pupil_timestep = set()

    start_lesson = input_data['lesson'][0]
    finish_lesson = input_data['lesson'][1]
    for second in range(start_lesson, finish_lesson):
        lesson_timestep.add(second)

    quantity_pupil_timestep = len(input_data['pupil'])
    for interval in range(0, quantity_pupil_timestep, 2):
        start_interval = input_data['pupil'][interval]
        finish_interval = input_data['pupil'][interval + 1]
        for second in range(start_interval, finish_interval + 1):
            pupil_timestep.add(second)

    quantity_tutor_timestep = len(input_data['tutor'])
    for interval in range(0, quantity_tutor_timestep, 2):
        start_interval = input_data['tutor'][interval]
        finish_interval = input_data['tutor'][interval + 1]
        for second in range(start_interval, finish_interval + 1):
            tutor_timestep.add(second)

    total_time = len(lesson_timestep.intersection(pupil_timestep.intersection(tutor_timestep)))
    return total_time


@app.route('/api', methods=['POST'])
def appearance_group():
    """Return total time of attendance at the lesson of students and teachers.
        It accepts data of the form:
            dict = [{
                    "id": PRIMARY KEY,
                    "lesson": [start_timestep, finish_timestep],
                    "pupil": [start_timestep1, finish_timestep1, start_timestep2, finish_timestep2, ...],
                    "tutor": [start_timestep1, finish_timestep1, start_timestep2, finish_timestep2, ...],
            },
            {
                    "id": PRIMARY KEY,
                    "lesson": [start_timestep, finish_timestep],
                    "pupil": [start_timestep1, finish_timestep1, start_timestep2, finish_timestep2, ...],
                    "tutor": [start_timestep1, finish_timestep1, start_timestep2, finish_timestep2, ...],
            },
        It returns data of the form:
            dict = [{
                    "id:": PRIMARY KEY,
                    "second": total_time,
                    "error_message": "Error"
            },
            {
                    "id:": PRIMARY KEY,
                    "second": total_time,
                    "error_message": "Error"
            }]
        """
    input_data = request.get_json()
    output_data = []

    for data in input_data:
        try:
            second = appearance(data)
            output_data.append({
                "id": f"{data['id']}",
                "second": f"{second}",
                "error_message": "Success"
            })
        except KeyError:
            output_data.append({
                    "id": f"{data['id']}",
                    "second": "None",
                    "error_message": "Wrong format data"
            })
    return jsonify(output_data)


if __name__ == '__main__':
    app.debug = True
    app.run()
