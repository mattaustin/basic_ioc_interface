import React from 'react'
import { withStyles } from '@material-ui/core/styles';

const styles = theme => ({
    success: {
        color: theme.palette.success.main,
    },
    warning: {
        color: theme.palette.warning.main,
    },
    error: {
        color: theme.palette.error.main,
    },
});

function ReadyState(props) { 
    const { readyState, classes } = props;
    if (readyState === 0) return <span className={classes.warning}>Connecting <i className="fas fa-exclamation"/></span>
    if (readyState === 1) return <span className={classes.success}>Connected <i className="fas fa-check"/></span>
    if (readyState === 2) return <span className={classes.warning}>Disconnecting <i className="fas fa-exclamation-triangle"/></span>
    if (readyState === 3) return <span className={classes.error}>Disconnected <i className="fas fa-exclamation"/></span>
    return <span className={classes.error}>Error <i className="fas fa-exclamation-triangle"/></span>
}

export default withStyles(styles)(ReadyState)