$begin 'Profile'
	$begin 'ProfileGroup'
		StartInfo='Time:  01/31/2019 12:55:08; Host: HATLAB-PC; Processor: 4; OS: NT 6.1; HFSS 2017.0.0'
		TotalInfo='Time:  01/31/2019 12:55:13, Status: Normal Completion'
		ProfileTask('', 0, 0, 0, 0, 0, 'Executing from C:\\Program Files\\AnsysEM\\AnsysEM18.0\\Win64\\HFSSCOMENGINE.exe', false, true)
		ProfileTask('RAM Limit', 0, 0, 0, 0, 0, 'hatlab-PC = 90.000000%', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Solution Basis Order: 1', false, true)
		ProfileTask('  Mesh TAU', 0, 0, 1, 0, 30000, '2312 tetrahedra', true, true)
		ProfileTask('  Mesh TAU (Coarsening)', 1, 0, 1, 0, 30000, '529 tetrahedra', true, true)
		ProfileTask('  Mesh Post', 0, 0, 0, 0, 30948, '529 tetrahedra', true, true)
		ProfileTask('Mesh Refinement', 0, 0, 0, 0, 0, 'Lambda Based', false, true)
		ProfileTask('  Mesh (lambda based)', 0, 0, 0, 0, 24812, '1363 tetrahedra', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 1', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 24264, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 31840, 'Disk = 0 KBytes, 1363 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 54252, 'Disk = 588 KBytes, matrix size 7536, matrix bandwidth  19.0, 27 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 54252, 'Disk = 1818 KBytes, 5 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 2', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('  Mesh (volume, adaptive)', 0, 0, 0, 0, 24828, '1781 tetrahedra', true, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 24796, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 34964, 'Disk = 0 KBytes, 1781 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 64920, 'Disk = 201 KBytes, matrix size 10112, matrix bandwidth  19.6, 34 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 64920, 'Disk = 2229 KBytes, 5 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Adaptive Passes converged', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Solution Process', 0, 0, 0, 0, 0, 'Elapsed time : 00:00:05 , Hfss ComEngine Memory : 40.7 M', false, true)
	$end 'ProfileGroup'
$end 'Profile'
