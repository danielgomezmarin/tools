def syncopation16(patt):
# compute syncopation value for 16 step pattern
# using the lhl methodology plus our notion of "awareness" introduced in these papers: 
# "Strictly Rhythm: Exploring the Effects of Identical Regions and Meter Induction in Rhythmic Similarity Perception"
# "PAD AND SAD: TWO AWARENESS-WEIGHTED RHYTHMIC SIMILARITY DISTANCES"
# presented at cmmr 2015 and ismir 2016 respectively.
# syncopation is the diference between the expecation at a silence and the expectation of the note preceeding it.
# awareness suggests interpulse sections within a bar have a different importance when measuring similarity,
# thus, this importance could be applied to expand the measure of syncopation:
# i.e. a syncopation on the first quarter of a bar is more important than the same syncopation located elsewhere

	synclist=[0]*16
	salience=[5,1,2,1,3,1,2,1,4,1,2,1,3,1,2,1]
	awareness=[5,1,4,2]
	for s,step in enumerate(patt):
		if patt[s]==1 and patt[(s+1)%16]==0: #look for an onset and a silence following
			synclist[s]=salience[(s+1)%16]-salience[s] #compute syncopations

	sync_and_awareness=[sum(synclist[0:4])*awareness[0],sum(synclist[4:8])*awareness[1],sum(synclist[8:12])*awareness[2], sum(synclist[12:16])*awareness[3]] # apply awareness
	output =sum(sync_and_awareness)
	
	return output
