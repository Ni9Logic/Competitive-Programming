input_lines = (
    "please sit spot. sit spot, sit. spot here now here.",
    "one, two. one tree. four tree. four four. five four. six five."
)

def each_word_and_its_follower(input_line):
    input_line = iter(input_line)
    current_word = next(input_line)
    for next_word in input_line:
        yield (current_word, next_word)
        current_word = next_word
    yield (current_word, '')

for input_line in input_lines:
    previous_input = ''
    current_input = input_line
    while (previous_input != current_input):

        previous_input = current_input
        splitted_input = current_input.split()

        rule_1_words = set(
            follower.rstrip(',.') 
            for (current_word, follower) in each_word_and_its_follower(splitted_input) 
            if current_word.endswith(',')
        )
        
        rule_2_words = set(
            current_word.rstrip(',.') 
            for current_word in splitted_input 
            if current_word.endswith(',')
        )

        def modify_words(previous_line):
            for (current_word, follower) in each_word_and_its_follower(previous_line):
                if current_word.endswith('.'):
                    yield current_word
                else:
                    if (follower.rstrip(',.') in rule_1_words) or (current_word.rstrip(',.') in rule_2_words):
                        yield f'{current_word.rstrip(",.")},'
                    else:
                        yield current_word

        current_input = ' '.join(modify_words(splitted_input))

    print('Input:', input_line, '\nOutput:', current_input, '\n')