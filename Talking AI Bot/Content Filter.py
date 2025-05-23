import openai

openai.api_key = ("redacted")

content_to_classify = "Fuck You"

output_label = None

response = openai.Completion.create(
      engine="content-filter-alpha-c4",
      prompt = content_to_classify,
      temperature=0,
      max_tokens=1,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      logprobs=10
    )


def filter(output_label):
     
     output_label = response["choices"][0]["text"]

     # This is the probability at which we evaluate that a "2" is likely real
     # vs. should be discarded as a false positive
     toxic_threshold = -0.355

     if output_label == "2":
         # If the model returns "2", return its confidence in 2 or other output-labels
         logprobs = response["choices"][0]["logprobs"]["top_logprobs"][0]

         # If the model is not sufficiently confident in "2",
         # choose the most probable of "0" or "1"
         # Guaranteed to have a confidence for 2 since this was the selected token.
         if logprobs["2"] < toxic_threshold:
             logprob_0 = logprobs.get("0", None)
             logprob_1 = logprobs.get("1", None)

             # If both "0" and "1" have probabilities, set the output label
             # to whichever is most probable
             if logprob_0 is not None and logprob_1 is not None:
                 if logprob_0 >= logprob_1:
                     output_label = "0"
                 else:
                     output_label = "1"
             # If only one of them is found, set output label to that one
             elif logprob_0 is not None:
                 output_label = "0"
             elif logprob_1 is not None:
                 output_label = "1"

             # If neither "0" or "1" are available, stick with "2"
             # by leaving output_label unchanged.

     # if the most probable token is none of "0", "1", or "2"
     # this should be set as unsafe
     if output_label not in ["0", "1", "2"]:
         output_label = "2"
         
     print ('output label is: '+output_label)

     return output_label


filter(output_label)

print (response)
