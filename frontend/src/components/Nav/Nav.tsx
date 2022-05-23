import React from "react";
import { AppBar, Toolbar, Typography } from "@material-ui/core";
import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  NavLink,
} from "react-router-dom";

import Inicio from "../Inicio/Inicio";
import Flota from "../Fleet/Fleet";

import "./Nav.css";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      flexGrow: 1,
    },
    offset: theme.mixins.toolbar,
    menuButton: {
      marginRight: theme.spacing(2),
    },
    title: {
      flexGrow: 1,
    },
  })
);

function Nav(): JSX.Element {
  const classes = useStyles();

  return (
    <>
      <Router>
        <div className={classes.root}>
          <AppBar position="sticky">
            <Toolbar>
              <img
                src="https://webkonce.cl/wp-content/uploads/2018/08/Phoenix_logo-600x563.png"
                width="40px"
                height="40px"
              />
              <Typography variant="h6" className={classes.title}>
                Flota de operaciones
              </Typography>

              <div className="btn-group">
                <Link to="/" className="btn btn-dark">
                  Inicio
                </Link>
              </div>
              <div className="btn-group">
                <Link to="/flota" className="btn btn-dark">
                  Flota
                </Link>
              </div>
            </Toolbar>
          </AppBar>
          <hr />
          <Switch>
            <Route path="/" exact>
              <Inicio />
            </Route>
            <Route path="/flota" exact>
              <Flota />
            </Route>
          </Switch>
        </div>
      </Router>
    </>
  );
}

export default Nav;
