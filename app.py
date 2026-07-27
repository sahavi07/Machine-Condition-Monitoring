#SIH 2026 Machine Condition Monitoring
from flask import Flask,jsonify
app=Flask(_name_)
@app.route('/')
def home():
  return jsonify({"status":"healthy","project":"Machine Condition Monitoring"})
  if_name_=='_main_':
  app.run(debug=True)
