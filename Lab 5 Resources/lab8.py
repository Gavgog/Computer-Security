'''
probability_spam_is_true_given_obs = prior
probability_spam_is_false_given_obs = 1 - prior


prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, False, False)

probability_spam_is_true_given_obs = prior * 0.3 * 0.05 * 0.7
probability_spam_is_false_given_obs = (1 - prior) * 0.001 * (1 - 0.05) * (1-0.7)


At the end we need:

probability_spam_is_true + probability_spam_is_false = 1


'''



def posterior(prior, likelihood, observation):
    t_result = prior
    for i in range(0,len(likelihood)):
        tf = observation[i]# true or false
        prob = likelihood[i][1]#get likelyhood of it being true
        if tf:#do one minus if its false
            t_result *= prob
        else:
            t_result *= 1-prob

    f_result = 1 - prior
    for i in range(0,len(likelihood)):
        tf = observation[i]# true or false
        prob = likelihood[i][0]#get likelyhood of it being false
        if tf:#do one minus if its false
            f_result *= prob
        else:
            f_result *= 1-prob

    total = f_result + t_result#normalise
    result = t_result / total

    return result

prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (False, False, False)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))