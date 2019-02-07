$begin 'Profile'
	$begin 'ProfileGroup'
		StartInfo='Time:  01/30/2019 11:40:49; Host: HATLAB-PC; Processor: 4; OS: NT 6.1; HFSS 2017.0.0'
		TotalInfo='Time:  01/30/2019 11:40:54, Status: Normal Completion'
		ProfileTask('', 0, 0, 0, 0, 0, 'Executing from C:\\Program Files\\AnsysEM\\AnsysEM18.0\\Win64\\HFSSCOMENGINE.exe', false, true)
		ProfileTask('RAM Limit', 0, 0, 0, 0, 0, 'hatlab-PC = 90.000000%', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Solution Basis Order: 1', false, true)
		ProfileTask('  Mesh TAU', 1, 0, 1, 0, 41000, '3465 tetrahedra', true, true)
		ProfileTask('  Mesh TAU (Coarsening)', 1, 0, 1, 0, 41000, '1843 tetrahedra', true, true)
		ProfileTask('  Mesh Post', 1, 0, 0, 0, 41764, '1843 tetrahedra', true, true)
		ProfileTask('Mesh Refinement', 0, 0, 0, 0, 0, 'Lambda Based', false, true)
		ProfileTask('  Mesh (lambda based)', 0, 0, 0, 0, 26012, '1749 tetrahedra', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 1', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 25072, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 27948, 'Disk = 0 KBytes, 634 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 39884, 'Disk = 137 KBytes, matrix size 2928, matrix bandwidth  14.7, 21 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 39884, 'Disk = 539 KBytes, 3 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 2', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('  Mesh (volume, adaptive)', 0, 0, 0, 0, 25808, '1947 tetrahedra', true, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 25468, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 28724, 'Disk = 0 KBytes, 738 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 41048, 'Disk = 24 KBytes, matrix size 3456, matrix bandwidth  14.9, 23 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 41048, 'Disk = 558 KBytes, 3 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Adaptive Passes converged', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Solution Process', 0, 0, 0, 0, 0, 'Elapsed time : 00:00:04 , Hfss ComEngine Memory : 42.9 M', false, true)
	$end 'ProfileGroup'
$end 'Profile'
