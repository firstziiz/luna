import React from 'react'
import { Switch, Route } from 'react-router-dom'

import Layout from '../Core/Layout'
import SolvePage from './SolvePage'

const SolveRoutes = props => (
  <Layout>
    <Switch>
      <Route
        exact
        path={`${props.match.path}/`}
        component={SolvePage}
      />
      <Route
        exact
        path={`${props.match.path}/:id`}
        component={SolvePage}
      />
    </Switch>
  </Layout>
)

export default SolveRoutes
