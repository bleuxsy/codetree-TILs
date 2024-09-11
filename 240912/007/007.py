class Note:
    def __init__(self, secret, meeting, time):
        self.secret = secret
        self.meeting = meeting
        self.time = time

    def __str__(self):
        return (f"secret code : {self.secret}\n"
                f"meeting point : {self.meeting}\n"
                f"time : {self.time}")

# Read input
secret, meeting, time = input().split()

# Create an instance of Note
note1 = Note(secret, meeting, time)

# Print the instance
print(note1)