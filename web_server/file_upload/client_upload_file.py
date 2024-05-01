import requests
from server import FileDescription

url="http://localhost:8000/upload/"
files = {'aFile': ("ibu-claims-complaint-rules.pdf", open('./ibu-claims-complaint-rules.pdf', 'rb'), "application/pdf")}

fd= FileDescription(name="claim_complaint_rules", 
                    description="a set of rules to manage complaints", 
                    type="pdf",
                    file_name="ibu-claims-complaint-rules.pdf")

response = requests.post(url, params=fd , files=files)

print(response.text.encode("utf-8"))