import os
import sample



def sequence_gen(model_path, model_param, vocab, seq_len, temperature, top_k, top_p, nucleus_sampling, context):
	sg = sample.SequenceGenerator(model_path, model_param, vocab)
	sg.load_weights()
	generated_seq = sg.sample_sequence(context,
									   seq_len=seq_len,
									   temperature=temperature,
									   top_k=top_k,
									   top_p=top_p,
									   nucleus_sampling=nucleus_sampling)
	f = open('s.txt','w',encoding = 'utf-8')
	f.write(generated_seq)
	f.close()
	
