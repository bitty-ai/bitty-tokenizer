## Testing Your Custom Tokenizer

To evaluate the accuracy of your custom tokenization method, follow these steps:

1. **Download the sample dataset**:  
   [tiny_sample_5M.txt](https://huggingface.co/datasets/itsmohit/Tiny-Stories-5M/raw/main/tiny_sample_5M.txt)

2. **Run your tokenization code** on this dataset.

3. **Compare the generated vocabulary**:  
   Your tokenizer's output vocabulary should exactly match the reference vocabulary provided at `test/vocab.json`.

This process will help you verify the correctness and consistency of your tokenization implementation.

Additionally you can use code in the compare.py file as a reference

The reason for this is there are many small-small aka bitty :) factors that can creep in unknowingly when training an tokenizer for a detailed version on this part please see the 'caveats' section in the medium article 
