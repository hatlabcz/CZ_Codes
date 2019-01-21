$begin 'Profile'
	$begin 'ProfileGroup'
		StartInfo='Time:  11/14/2018 10:50:06; Host: HATLAB-PC; Processor: 4; OS: NT 6.1; HFSS 2017.0.0'
		TotalInfo='Time:  11/14/2018 10:50:11, Status: Normal Completion'
		ProfileTask('', 0, 0, 0, 0, 0, 'Executing from C:\\Program Files\\AnsysEM\\AnsysEM18.0\\Win64\\HFSSCOMENGINE.exe', false, true)
		ProfileTask('RAM Limit', 0, 0, 0, 0, 0, 'hatlab-PC = 90.000000%', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Solution Basis Order: 1', false, true)
		ProfileTask('  Mesh stitch', 0, 0, 0, 0, 26316, '112 triangles', true, true)
		ProfileTask('  Mesh Classic', 0, 0, 0, 0, 26828, '255 tetrahedra', true, true)
		ProfileTask('  Mesh Post', 0, 0, 0, 0, 27180, '86 tetrahedra', true, true)
		ProfileTask('Mesh Refinement', 0, 0, 0, 0, 0, 'Manual Seed Based', false, true)
		ProfileTask('  Mesh (volume, seed)', 0, 0, 0, 0, 24584, '576 tetrahedra', true, true)
		ProfileTask('Mesh Refinement', 0, 0, 0, 0, 0, 'Lambda Based', false, true)
		ProfileTask('  Mesh (lambda based)', 0, 0, 0, 0, 23956, '613 tetrahedra', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'cavity', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 1', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 23384, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 26872, 'Disk = 0 KBytes, 613 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 39880, 'Disk = 251 KBytes, matrix size 3214, matrix bandwidth  17.5, 23 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 39880, 'Disk = 817 KBytes, 5 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Adaptive Pass 2', 0, 0, 0, 0, 0, 'Eigenmode Solution', false, true)
		ProfileTask('  Mesh (volume, adaptive)', 0, 0, 0, 0, 24068, '804 tetrahedra', true, true)
		ProfileTask('Simulation Setup', 0, 0, 0, 0, 23624, 'Disk = 0 KBytes', true, true)
		ProfileTask('Matrix Assembly', 0, 0, 0, 0, 28208, 'Disk = 0 KBytes, 804 tetrahedra ', true, true)
		ProfileTask('EigenSolver DRS1', 0, 0, 0, 0, 43388, 'Disk = 88 KBytes, matrix size 4346, matrix bandwidth  18.3, 23 eigen iterations', true, true)
		ProfileTask('Field Recovery', 0, 0, 0, 0, 43388, 'Disk = 1005 KBytes, 5 computed eigenmodes', true, true)
		ProfileTask('', 0, 0, 0, 0, 0, 'Adaptive Passes converged', false, true)
		ProfileTask('', 0, 0, 0, 0, 0, '', false, true)
		ProfileTask('Solution Process', 0, 0, 0, 0, 0, 'Elapsed time : 00:00:04 , Hfss ComEngine Memory : 41.4 M', false, true)
	$end 'ProfileGroup'
$end 'Profile'
