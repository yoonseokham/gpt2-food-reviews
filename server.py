from flask import Flask, render_template, request, Response, send_file, jsonify
import requests
import json

# Server & Handling Setting
app = Flask(__name__)


# def run_model(prompt, num=1, length=30):
#    try:
#        prompt = prompt.strip()
#        input_ids = tokenizer.encode(prompt, return_tensors='pt')
#
#        # input_ids also need to apply gpu device!
#        input_ids = input_ids.to(device)
#
#        min_length = len(input_ids.tolist()[0])
#        length += min_length
#
#        # model = models[model_name]
#        sample_outputs = model.generate(input_ids, pad_token_id=50256,
#                                        do_sample=True,
#                                        max_length=300,
#                                        top_k=50,
#                                        num_return_sequences=num)
#        generated_texts = ""
#        for i, sample_output in enumerate(sample_outputs):
#            output = tokenizer.decode(sample_output.tolist(),skip_special_tokens=False)
#            generated_texts+= output+'\n'
#        generated_texts.replace("<br/>",'\n')
#        generated_texts.replace("<br />",'\n')
#        return generated_texts

#    except Exception as e:
#        print(e)
#        return 500



# @app.route("/gpt2-recipes-maker/", methods=['POST'])

@app.route("/api/", methods=['GET'])
def generate():
    try:
        review = request.args.get('review')
        data = {
            "text": review,
            "num_samples": 1,
            "length": 30
        }
        URL = "https://feature-add-torch-serve-gpt-2-server-gkswjdzz.endpoint.ainize.ai/infer/dilstilgpt2-finetuned-amazon-food-reviews"
        headers = {
                "Content-Type": "application/json",
        }
        res = requests.post(URL, headers=headers, data=json.dumps(data))
        res = res.json()
        return res
    except Exception as e:
        return jsonify(e), 500

# Health Check
@app.route('/healthz')
def health():
    return "ok", 200


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
