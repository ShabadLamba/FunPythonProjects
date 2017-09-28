def move_one_policemen_rl(current_state):
	if(current_state['rpolicemen'] != 0):
		current_state['rpolicemen'] -= 1
		current_state['lpolicemen'] += 1
	return current_state

def move_one_policemen_lr(current_state):
	if(current_state['lpolicemen'] != 0):
		current_state['rpolicemen'] += 1
		current_state['lpolicemen'] -= 1
	return current_state


def move_one_prisioner_rl(current_state):
	if(current_state['rprisoners'] != 0):
		current_state['rprisoners'] -= 1
		current_state['lprisoners'] += 1
	return current_state

def move_one_prisioner_lr(current_state):
	if(current_state['lprisoners'] != 0):
		current_state['rprisoners'] += 1
		current_state['lprisoners'] -= 1
	return current_state


def move_two_policemen_rl(current_state):
	if(current_state['rpolicemen'] > 1):
		current_state['rpolicemen'] -= 2
		current_state['lpolicemen'] += 2
	return current_state


def move_two_policemen_lr(current_state):
	if(current_state['lpolicemen'] > 1):
		current_state['rpolicemen'] += 2
		current_state['lpolicemen'] -= 2
	return current_state

def move_two_prisioner_rl(current_state):
	if(current_state['rprisoners'] > 1):
		current_state['rprisoners'] -= 2
		current_state['lprisoners'] += 2
	return current_state

def move_two_prisioner_lr(current_state):
	if(current_state['lprisoners'] > 1):
		current_state['rprisoners'] += 2
		current_state['lprisoners'] -= 2
	return current_state


def move_one_policemenandprisioner_rl(current_state):
	if(current_state['rprisoners'] != 0 and current_state['rpolicemen'] != 0):
		current_state['rpolicemen'] -= 1
		current_state['rprisoners'] -= 1
		current_state['lpolicemen'] += 1
		current_state['lprisoners'] += 1
	return current_state


def move_one_policemenandprisioner_lr(current_state):
	if(current_state['lprisoners'] != 0 and current_state['lpolicemen'] != 0):
		current_state['rpolicemen'] += 1
		current_state['rprisoners'] += 1
		current_state['lpolicemen'] -= 1
		current_state['lprisoners'] -= 1
	return current_state
