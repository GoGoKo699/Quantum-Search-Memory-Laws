"""Finite-dimensional checks of the hidden-memory lower-bound invariant.

The general proof is in science/lower-bounds.md. The fixed seed makes the
sampled controls reproducible; this computation does not prove universality.
"""
import numpy as np


def run():
    rng=np.random.default_rng(20261018)
    N, anc, T=4,3,12
    D=N*anc
    deltas=[0.001,0.01,0.1,0.25,0.5,0.75,0.9,0.99,0.999]
    def unitary():
        z=rng.normal(size=(D,D))+1j*rng.normal(size=(D,D))
        q,r=np.linalg.qr(z)
        diag=np.diag(r)
        return q @ np.diag(diag/np.abs(diag))
    def outer(v):
        return np.outer(v,v.conj())
    rows=[]
    for scenario,delta in [(s,d) for s in ['phase_calls','bit_calls_and_idle_slots'] for d in deltas]:
        kappa=1-2*delta
        beta=2/(1+kappa*kappa)
        A=2*(1+kappa*kappa)/(1-kappa*kappa)
        psi=rng.normal(size=D)+1j*rng.normal(size=D)
        psi/=np.linalg.norm(psi)
        phi=np.tile(psi,(N,2,1))
        rho=np.tile(outer(psi),(N,2,1,1))
        oldV=np.zeros(N)
        min_eig=1.0
        max_excess=-np.inf
        max_sum_excess=-np.inf
        max_trace_error=0.0
        for t in range(T):
            U=unitary()
            psi_next=U@psi
            enabled=(scenario=='phase_calls' or t%4!=2)
            response_projector=np.eye(anc) if scenario=='phase_calls' else np.diag([0,1,0])
            if not enabled:
                response_projector=np.zeros((anc,anc))
            total_projector=np.kron(np.eye(N),response_projector)
            newV=np.zeros(N)
            for w in range(N):
                P=np.zeros((D,D),complex)
                P[w*anc:(w+1)*anc,w*anc:(w+1)*anc]=response_projector
                O=np.eye(D)-2*P
                f0,f1=phi[w,0].copy(),O@phi[w,1]
                r0,r1=rho[w,0].copy(),O@rho[w,1]@O
                phi[w,0]=U@((1-delta)*f0+delta*f1)
                phi[w,1]=U@(delta*f0+(1-delta)*f1)
                rho[w,0]=U@((1-delta)*r0+delta*r1)@U.conj().T
                rho[w,1]=U@(delta*r0+(1-delta)*r1)@U.conj().T
                s=(phi[w,0]+phi[w,1])/2
                d=(phi[w,0]-phi[w,1])/2
                newV[w]=np.linalg.norm(psi_next-s)**2+beta*np.linalg.norm(d)**2
                for b in (0,1):
                    residual=rho[w,b]-outer(phi[w,b])
                    min_eig=min(min_eig,float(np.linalg.eigvalsh(residual).min()))
                    max_trace_error=max(max_trace_error,float(abs(np.trace(rho[w,b])-1)))
                joint_rho=(rho[w,0]+rho[w,1])/2
                residual=joint_rho-outer(s)-outer(d)
                min_eig=min(min_eig,float(np.linalg.eigvalsh(residual).min()))
                upper=A*np.linalg.norm(P@psi)**2
                max_excess=max(max_excess,float(newV[w]-oldV[w]-upper))
            max_sum_excess=max(max_sum_excess,float(np.sum(newV-oldV)-A*np.linalg.norm(total_projector@psi)**2))
            oldV=newV
            psi=psi_next
        if not min_eig>-1e-10:
            raise AssertionError("Conditional PSD remainder failed")
        if not max_excess<1e-9:
            raise AssertionError("One-step potential bound failed")
        if not max_sum_excess<1e-9:
            raise AssertionError("Summed potential bound failed")
        if not max_trace_error<1e-10:
            raise AssertionError("Conditional trace normalization failed")
        rows.append({"scenario":scenario,"delta":delta,"minimum_PSD_residual_eigenvalue":min_eig,
                     "largest_one_step_bound_excess":max_excess,
                     "largest_summed_bound_excess":max_sum_excess,
                     "maximum_conditional_trace_error":max_trace_error})
    result={"purpose":"Finite numerical invariant check; universal claims use the analytical proof",
            "seed":20261018,"N":N,"ancilla_dimension":anc,"steps":T,"passed":True,"checks":rows}
    return result
