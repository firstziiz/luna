const Router = require('express').Router
const router = Router()

const helloRoutes = require('./api/hello/routes')
const solveRoutes = require('./api/solve/routes')
const tasksRoutes = require('./api/tasks/routes')

router.get('/', async (req, res) => {
  res.status(200).send({
    status: `[${process.env.PROJECT_NAME}] API Server is running!`
  })
})

router.use('/hello', helloRoutes)
router.use('/solve', solveRoutes)
router.use('/tasks', tasksRoutes)

module.exports = router
