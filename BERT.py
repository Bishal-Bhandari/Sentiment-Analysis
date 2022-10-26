from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class BertAnalysis:
    def bert_analysis(self):
        # loading the pretrained model
        tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
        model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

        # tokenizing the data
        tokens = tokenizer.encode(self, return_tensors='pt')
        result = model(tokens)
        final_result = int(torch.argmax(result.logits))+1

        return str(final_result)

