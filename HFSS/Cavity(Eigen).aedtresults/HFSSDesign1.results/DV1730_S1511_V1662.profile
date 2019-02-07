$begin 'Profile'
	$begin 'ProfileGroup'
		StartInfo='Time:  01/31/2019 14:24:29; Host: HATLAB-PC; Processor: 4; OS: NT 6.1; HFSS 2017.0.0'
		TotalInfo='Time:  01/31/2019 14:24:43, Status: Normal Completion'
		ProfileTask('', 0, 0, 0, 0, 0, 'Executing from C:\\Program Files\\AnsysEM\\AnsysEM18.0\\Win64\\HFSSCOMENGINE.exe', false, true)
		ProfileTask('RAM Limit', 0, 0, 0, 0, 0, 'hatlab-PC = 90.000000%', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Solution Basis Order: 1', false, true)
		ProfileTask('  Mesh TAU', 2, 0, 1, 0, 56000, '25844 tetrahedra', true, true)
		ProfileTask('  Mesh TAU (Coarsening)', 1, 0, 1, 0, 56000, '8422 tetrahedra', true, true)
		ProfileTask('  Mesh Post', 1, 0, 0, 0, 57780, '8422 tetrahedra', true, true)
		ProfileTask('Mesh Refinement', 0, 0, 0, 0, 0, 'Lambda Based', false, true)
		ProfileTask('  Mesh (lambda based)', 1, 0, 1, 0, 33332, '8154 tetrahedra', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 1', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 34428, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 51276, 'Disk = 0 KBytes, 4353 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 94632, 'Disk = 3349 KBytes, matrix size 21436, matrix bandwidth  16.1, 34 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 94632, 'Disk = 11079 KBytes, 10 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 2', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('  Mesh (volume, adaptive)', 0, 0, 0, 0, 33184, '9462 tetrahedra', true, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 36008, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 60032, 'Disk = 0 KBytes, 5548 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 1, 0, 1, 0, 122784, 'Disk = 1150 KBytes, matrix size 28796, matrix bandwidth  17.4, 37 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 122784, 'Disk = 13653 KBytes, 10 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Adaptive Passes converged', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Solution Process', 0, 0, 0, 0, 0, 'Elapsed time : 00:00:14 , Hfss ComEngine Memory : 45.7 M', false, true)
	$end 'ProfileGroup'
$end 'Profile'
